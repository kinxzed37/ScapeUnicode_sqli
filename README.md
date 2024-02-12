# ScapeUnicode_sqli
### Scape Unicode SQLInjection

This script is useful to bypass weak filtering and/or WAFs in JSON contexes

## Install Requierements for the script
 ```shell
 pip install pwn
 ```
## Before Use
**You need to change the follow variables in the code according to you victim**

main_url = `URL Where u need to do SQLi`

BurpSuite_Proxy = `If u have a proxy`

headers = `Content-Type but u can use the actual`

post_data = `specify where to instert the payload with a %s`


REQUEST = `In default is set to use the proxy but if u delete "proxies=BurpSuite_Proxy" u can use without it`

## Usage
```shell
python3 SQLi.py
>
```


