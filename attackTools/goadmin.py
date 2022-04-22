# -*-codeing = utf-8 -*-
import os
import re
import time
from multiprocessing import Pool

import requests
import threading

i = -1
urls_txt = []
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


def url_list(txt):
    global urls_txt
    with open(txt, mode='r',encoding='utf-8') as fp:
        urls_txt = fp.readlines()

def return_url():
    global i
    i += 1
    url = urls_txt[i].replace('\n', '').replace('\r', '')
    return url

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            try:
                url = return_url()
                print(f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   {self.name} start: ',url)
                crawler(url,self.name)
            except:
                break
        print(f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   Thread exit: ' + self.name)


# 定义功能函数，访问固定url地址

admin_list = ['admin','Admin','后台','管理','manage','运营','登录','login','adm']
admin_dir = ['/admin','/manage','/admin/login','/manage/login','/admin/index','/manage/index','/admin/login/index','/admin/login.php','/manage/index.php']
def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    try:
        for adminDir in admin_dir:
            url = url_+adminDir
            requests.packages.urllib3.disable_warnings()
            resuit = requests.get(url,headers=header,timeout=10,verify=False)
            resuit_text = resuit.text
            ex = '<title>(.*?)</title>'
            title = re.findall(ex, resuit_text, re.S)[0]
            if resuit.status_code <= 399:
                for admin in admin_list:
                    if admin in title:
                        print(f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: ', url,title)
                        PocSuccess(url)
                break


    except Exception as e:
        print(f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   {ts} ==> {url_} ==> Error')


def PocSuccess(success):
    with open('Admin.txt', mode='a+', encoding='UTF-8-sig') as fp:
        fp.write(success + "\n")

def loadPoc(url):
    poc_list = []

    return poc_list


# 创建线程列表
def goRun(txt,T):
    threads = []
    url_list(txt)
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
if __name__ == '__main__':
    goRun("demo.txt",50)