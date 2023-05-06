   # 🪐  &nbsp;  LFI-SPACE TOOL  &nbsp;  🪐

<img src="https://i.imgur.com/KuLbSJP.png" width="70%"></img>



#### Written by TMRSWRR 
#### Version 1.0.0
All in one tools for **LFI VULN FINDER -LFI DORK FINDER**

Instagram: [TMRSWRR](https://www.instagram.com/tmrswrr/)
##  :camera: Screenshots  :camera:

<img src="https://i.imgur.com/Hzr41Hm.jpg" width="32%"></img>
<img src="https://i.imgur.com/FeHo1Og.jpg" width="32%"></img>
<img src="https://i.imgur.com/CRuf1l2.png" width="32%"></img>

## 👇 💫  How to use  💫 👇

[![How to use](https://i.imgur.com/ybDgF57.png)](https://youtu.be/rpcGqwZU2As)

## 📒 Read Me 📒

*LFI Space is a robust and efficient tool designed to detect Local File Inclusion (LFI) vulnerabilities in web applications. This tool simplifies the process of identifying potential security flaws by leveraging two distinct scanning methods: Google Dork Search and Targeted URL Scan. With its comprehensive approach, LFI Space assists security professionals, penetration testers, and ethical hackers in assessing the security posture of web applications.*

*The Google Dork Search functionality within LFI Space harnesses the power of the Google search engine to identify web pages that may be susceptible to LFI attacks. By employing carefully crafted Google dorks, the tool retrieves search results that are likely to contain vulnerable pages. These dorks are specific queries designed to target common LFI vulnerability patterns in web applications. LFI Space then analyzes the responses from these pages, meticulously examining the content to identify any signs of LFI vulnerabilities. This approach allows for a broad and automated search, rapidly surfacing potential targets for further investigation.*

*Additionally, LFI Space provides a Targeted URL Scan feature, enabling users to manually input a list of specific URLs for scanning. This functionality allows for a more focused approach, enabling security professionals to assess particular web applications or pages of interest. By scanning each URL individually, LFI Space thoroughly inspects the target web pages for any signs of LFI vulnerabilities. This targeted approach provides flexibility and precision in identifying potential security weaknesses.*

*It is important to note that LFI Space is intended for responsible and authorized use, such as security testing, vulnerability assessments, or penetration testing, with proper consent and legal permissions. It is crucial to adhere to ethical guidelines and respect the privacy and security of targeted systems.*

*In conclusion, LFI Space is a powerful tool that combines Google Dork Search and Targeted URL Scan functionalities to detect Local File Inclusion vulnerabilities in web applications. By automating the search for potentially vulnerable pages and providing the ability to scan specific URLs, LFI Space empowers security professionals to identify LFI vulnerabilities effectively. With its user-friendly interface and comprehensive scanning capabilities, LFI Space is an invaluable asset for enhancing the security posture of web applications.*

* Google Dork Search: The tool queries the Google search engine to find web pages that may be vulnerable to LFI attacks based on carefully crafted Google dorks. It then analyzes the responses of these pages to determine if any LFI vulnerabilities exist.
 * Targeted URL Scan: The tool accepts a list of URLs as input and scans each URL for LFI vulnerabilities. This feature allows for a more focused approach, enabling users to assess specific web applications or pages of interest.
## 🍏 LFI Find Dork 🍏

```
inurl:/filedown.php?file=
inurl:/news.php?include=
inurl:/view/lang/index.php?page=?page=
inurl:/shared/help.php?page=
inurl:/include/footer.inc.php?_AMLconfig[cfg_serverpath]=
inurl:/squirrelcart/cart_content.php?cart_isp_root=
inurl:index2.php?to=
inurl:index.php?load=
inurl:home.php?pagina=
/surveys/survey.inc.php?path=
index.php?body=
/classes/adodbt/sql.php?classes_dir=
enc/content.php?Home_Path=
```
* This dork list in lfi2.txt file

##  :cd: Installation  :cd:
### Installation with requirements.txt

```bash
git clone https://github.com/capture0x/Lfi-Space/
cd Lfi-Space
pip3 install -r requirements.txt
```

## ⭐ Usage ⭐

```bash
python3 lfi.py
```

## Bugs and enhancements

For bug reports or enhancements, please open an [issue](https://github.com/capture0x/Lfi-Space/issues) here.


**Copyright 2023**
