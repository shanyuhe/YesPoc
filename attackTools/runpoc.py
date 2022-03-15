# -*-codeing = utf-8 -*-
import os
import time
from multiprocessing import Pool
import requests
import threading
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S")

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
                print(f"{otherStyleTime }   {self.name} start: ",url)
                crawler(url,self.name)
            except:
                break
        print(f"{otherStyleTime }   Thread exit: " + self.name)


# 定义功能函数，访问固定url地址


def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    try:
        pocPool(url_)

    except Exception as e:
        print(f"{otherStyleTime }   {ts} ==> {url_} ==> Error")


def PocSuccess(success):
    module_name = os.path.abspath(os.path.dirname(__file__))[:-11]
    with open(module_name+'/POCresuit.txt', mode='a+', encoding='UTF-8-sig') as fp:
        fp.write(success + "\n")

def attack_Poc(poc_url):
    module_name = poc_url['poc']
    url = poc_url['url']
    requests.packages.urllib3.disable_warnings()
    module = __import__(f'YESPoc.attackPoc.{module_name}', fromlist=['poc'])
    result = module.poc(url)
    pcosuccess = f"{otherStyleTime }   【{module_name}】{url}"
    if result == True:
        print(pcosuccess)
        PocSuccess(pcosuccess)

def loadPoc(url):
    poc_list = []
    module_name_list = os.listdir(os.path.abspath(os.path.dirname(__file__))[:-11]+"attackPoc")
    for script_name in module_name_list:
        if script_name not in ['__init__.py', 'test.py'] and os.path.splitext(script_name)[1] == '.py':
            module_name = os.path.basename(script_name).split(".")[0]
            poc_list.append({"poc":module_name,"url":url})
    return poc_list

# 协程请求
def pocPool(url):
    poc_dic = loadPoc(url)
    pool = Pool(20)
    pool.map(attack_Poc,poc_dic)
    pool.close()
    pool.join()

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