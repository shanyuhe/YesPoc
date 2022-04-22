# -*-codeing = utf-8 -*-
# @Time : {DATE}
# @Author : 一秋小叶　qq 2900180755
# @FIle ： {NAME}
# @Software : PyCharm
import requests


def poc(url_t):
    url_ = url_t.replace('\n', '').replace('\r', '')
    config = '/.git/config'
    try:
            url = url_ + config
            requests.packages.urllib3.disable_warnings()
            resuit = requests.get(url, timeout=10,verify=False)
            resuit_text = resuit.text
            if resuit.status_code == 200 and resuit_text.find("[core]") != -1:
                return True
            else:
                return False
    except Exception as a:
        return False
