# -*-codeing = utf-8 -*-
# @Time : {DATE}
# @Author : 一秋小叶　qq 2900180755
# @FIle ： {NAME}
# @Software : PyCharm

import requests



def poc(target_url):
    url = target_url
    r = requests.post(url,timeout=20,verify=False).text
    if r.find("There was an error.") != -1 :
        return True # 也可以返回1
    else: # 不存在信息泄露
        return False # 也可以返回0
