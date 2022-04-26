# -*-codeing = utf-8 -*-
# @Time : 2022/4/22
# @Author : 一秋小叶　qq 2900180755
# @FIle ： UA
# @Software : PyCharm
import os
import time
from multiprocessing import Pool
import requests
import threading
import sys
from lib.Tools.PrintLog import PrintLog
from lib.Tools.Time_Log import time_s

requests.packages.urllib3.disable_warnings()

sys.path.insert(0, './YESPoc')
sys.path.insert(0, './attackPoc')
i = -1
urls_txt = []
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}




def return_url():
    global i
    i += 1
    url = poc_list[i]
    return url

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            try:
                url = return_url()
                log = f"{time_s()}   {self.name} start: " + url['url']
                PrintLog(log)
                crawler(url,self.name)
            except:
                break
        log = f"{time_s()}   Thread exit: " + self.name
        PrintLog(log)


# 定义功能函数，访问固定url地址


def crawler(url_t,ts):
    try:
        attack_Poc(url_t)
    except Exception as e:
        log = f"{time_s()}   {ts} ==> {url_t['url']} ==> Error"
        PrintLog(log)


def PocSuccess(success):
    with open('200_PocResuit.txt', mode='a+', encoding='UTF-8-sig') as fp:
        fp.write(success + "\n")

def attack_Poc(poc_url):
    module_name = poc_url['poc']
    url = poc_url['url']
    requests.packages.urllib3.disable_warnings()
    module = __import__(f'attackPoc.{module_name}', fromlist=['poc'])
    result = module.poc(url)
    if result == True:
        log = f"{time_s()}   SUCCESS:【{module_name}】{url} True"
        print('\r'+log)
        PocSuccess(log)
    else:
        log = f"{time_s()}   【{module_name}】{url} ..."
        PrintLog(log)

# 协程请求

# 创建线程列表
def goRun(urls_file,poc,T):
    global name_txt
    name_txt =  "200_POC_"+ urls_file.replace('\\', '')
    threads = []
    loadPoc_url(urls_file, poc)
    # 开启线程数量
    print(f'Starting Thread  + {str(T)}')
    for i in range(T):
        # 给每个线程命名
        ts ="Thread-"+str(i+1)
        thread = myThread(ts)
        thread.start()
        # 将线程添加到线程列表
        threads.append(thread)
        time.sleep(0.1)

    # 等待所有线程完成
    for t in threads:
        t.join()


def loadPoc_url(urls_file,poc):
    global poc_list
    with open(urls_file, mode='r',encoding='utf-8') as fp:
        urls_txt = fp.readlines()
    poc_list = []
    for url in urls_txt:
        poc_list.append({"poc": poc, "url": url.replace('\n', '').replace('\r', '')})


if __name__ == '__main__':
    pass
    # goRun("./所有的.txt","laraverDeBug",20)
