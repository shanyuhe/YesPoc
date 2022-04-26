# -*-codeing = utf-8 -*-
# @Time : 2022/4/22
# @Author : 一秋小叶　qq 2900180755
# @FIle ： UA
# @Software : PyCharm
import os
import re
import sys
import time
from lib.Tools.PrintLog import PrintLog
import requests
import threading



requests.packages.urllib3.disable_warnings()

i = -1
urls_txt = []
name_txt = ''
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}




def url_list(txt):
    global name_txt
    global urls_txt
    name_txt = "200_Admin_"+ txt.replace('\\', '')
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
                log = f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   {self.name} start: '+url
                PrintLog(log)
                crawler(url,self.name)
            except:
                break
        log = f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   Thread exit: ' + self.name
        PrintLog(log)


# 定义功能函数，访问固定url地址

admin_list = ['adm','Admin','后台','管理','manage','运营','登录','login','系统']
admin_dir = ['/admin','/manage','/admin/login','/manage/login','/admin/index','/manage/index','/admin/login/index','/admin/login.php','/manage/index.php','/phpmyadmin']
def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    try:
        for adminDir in admin_dir:
            url = url_+adminDir
            log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   {url}'
            PrintLog(log)
            resuit = requests.get(url,headers=header,timeout=10,verify=False)
            resuit_text = resuit.text
            ex = '<title>(.*?)</title>'
            title = re.findall(ex, resuit_text, re.S)[0]
            if resuit.status_code <= 399:
                for admin in admin_list:
                    if admin in title:
                        log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   SUCCESS:{url}     {title} '
                        print('\r' + log)
                        PocSuccess(url)
                        break
                break

    except Exception as e:
        log = f'{(time.strftime("%Y-%m-%d %H:%M:%S")) }   {ts} ==> {url_} ==> Error'
        PrintLog(log)


def PocSuccess(success):
    with open(name_txt, mode='a+', encoding='UTF-8-sig') as fp:
        fp.write(success + "\n")



# 创建线程列表
def goRun(txt,T):
    threads = []
    url_list(txt)
    # 开启线程数量
    log = f'Starting Thread  + {str(T)}'
    PrintLog(log)
    for i in range(T):
        # 给每个线程命名
        ts ="Thread-"+str(i+1)
        thread = myThread(ts)
        thread.start()
        # 将线程添加到线程列表
        threads.append(thread)
    # 等待所有线程完成
    for t in threads:
        t.join()

if __name__ == '__main__':
    goRun("./所有的.txt",50)
