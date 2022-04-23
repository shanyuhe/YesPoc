# -*-codeing = utf-8 -*-
# @Time : 2022/4/22
# @Author : 一秋小叶　qq 2900180755
# @FIle ： UA
# @Software : PyCharm

import time
import requests
import threading
from lib.Tools.PrintLog import PrintLog
from lib.Tools.Time_Log import time_s
i = -1
urls_txt = []
name_txt = ''
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

requests.packages.urllib3.disable_warnings()

def url_list(txt):
    global name_txt
    global urls_txt
    name_txt =  "200_"+ txt.replace('\\', '')
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
                url  =  return_url()
                log = f'{time_s()}   {self.name} start: '+url
                print(
                    '\r' + '                                                                                                                                ',
                    end='')
                PrintLog(log)
                crawler(url,self.name)
            except:
                break
        log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   Thread exit: ' + self.name
        print(
            '\r' + '                                                                                                                                ',
            end='')
        PrintLog(log)


# 定义功能函数，访问固定url地址
def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    try:
        http_i = url_t.find("http")
        if http_i == -1:
            try:
                url = 'http://'+url_
                req = requests.get(url, headers=header, timeout=20,verify=False).status_code
                if req < 100000:
                    with open(name_txt, mode='a') as fp3:
                        fp3.write(url + '\n')
                        log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url} | {req}'
                        print(
                            '\r' + '                                                                                                                                ',
                            end='')
                        print('\r' + log)
            except Exception as e:
                try:
                    url = 'https://' + url_
                    req = requests.get(url, headers=header, timeout=20,verify=False).status_code
                    if req < 100000:
                        with open(name_txt, mode='a') as fp3:
                            fp3.write(url + '\n')
                            log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url} | {req}'
                            print(
                                '\r' + '                                                                                                                                ',
                                end='')
                            print('\r' + log)
                except Exception as e:
                    try:
                        url = 'http://www.' + url_
                        req = requests.get(url, headers=header, timeout=20,verify=False).status_code
                        if req < 100000:
                            with open(name_txt, mode='a') as fp3:
                                fp3.write(url + '\n')
                                log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url} | {req}'
                                print(
                                    '\r' + '                                                                                                                                ',
                                    end='')
                                print('\r' + log)
                    except Exception as e:
                        try:
                            url = 'https://www.' + url_
                            req = requests.get(url, headers=header, timeout=20,verify=False).status_code
                            if req < 100000:
                                with open(name_txt, mode='a') as fp3:
                                    fp3.write(url + '\n')
                                    log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url} | {req}'
                                    print(
                                        '\r' + '                                                                                                                                ',
                                        end='')
                                    print('\r' + log)
                        except Exception as e:
                            log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url} | Error'
                            print(
                                '\r' + '                                                                                                                                ',
                                end='')
                            PrintLog(log)


        else: # 带协议的url
            req = requests.get(url_, headers=header, timeout=20,verify=False).status_code
            if req < 100000:
                with open(name_txt, mode='a') as fp3:
                    fp3.write(url_ + '\n')
                    log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url_} | {req}'
                    print(
                        '\r' + '                                                                                                                                ',
                        end='')
                    print('\r' + log)
    except Exception as e:
        log = f'{(time.strftime("%Y-%m-%d %H:%M:%S"))}   resuit: {ts}  {url} | Error'
        print(
            '\r' + '                                                                                                                                ',
            end='')
        PrintLog(log)



# 创建线程列表
def goRun(txt,T):
    threads = []
    url_list(txt)
    # 开启线程数量
    log = f'Starting Thread  + {str(T)}'
    print(
        '\r' + '                                                                                                                                ',
        end='')
    PrintLog(log)
    for i in range(int(T)):
        # 给每个线程命名
        ts ="Thread-"+str(i)
        thread = myThread(ts)
        thread.start()
        # 将线程添加到线程列表
        threads.append(thread)
        time.sleep(0.1)

    # 等待所有线程完成
    for t in threads:
        t.join()


if __name__ == '__main__':
    goRun('存活.txt',100)