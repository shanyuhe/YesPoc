# -*-codeing = utf-8 -*-
# @Time : 2022/4/22
# @Author : 一秋小叶　qq 2900180755
# @FIle ： springboot-env
# @Software : PyCharm
import requests
from lib.Tools.UA import ua

def poc(url_t):
    url_ = url_t.replace('\n', '').replace('\r', '')
    config = '/actuator/env'
    try:
            url = url_ + config
            requests.packages.urllib3.disable_warnings()
            resuit = requests.get(url, timeout=10,headers=ua(),verify=False)
            resuit_text = resuit.text
            if resuit.status_code == 200 and resuit_text.find("activeProfiles") != -1:
                return True
            else:
                return False
    except Exception as a:
        return False

