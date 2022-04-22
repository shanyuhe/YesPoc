# -*-codeing = utf-8 -*-
# @Time : {DATE}
# @Author : 一秋小叶　qq 2900180755
# @FIle ： {NAME}
# @Software : PyCharm
import re
import time

import requests
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
proxies = {
    'http': '127.0.0.1:10809',
    'https': '127.0.0.1:10809',
}
def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    # try:
    url = url_
    requests.packages.urllib3.disable_warnings()
    resuit = requests.get(url,timeout=10,headers=header,proxies=proxies)
    resuit_text = resuit.text
    print(resuit_text)
    ex = "(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)"
    emails = re.findall(ex, resuit_text,re.S)
    if emails != []:
        print(f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: ', url,emails)
        for email in emails:
            print(email)
    # except Exception as e:
    #     print(f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   {ts} ==> {url_} ==> Error')


if __name__ == '__main__':
    pass