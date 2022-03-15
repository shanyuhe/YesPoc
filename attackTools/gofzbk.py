# -*-codeing = utf-8 -*-
import os

import os
import re
import requests
import random
import time
import threading
from multiprocessing.dummy import Pool


header = [
    {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"},
     {'User-Agent':"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"},
      {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"},
       {'User-Agent':"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"},
        {'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1"},
         {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"}]


houzhui = ['.gz', '.sql.gz', '.tar.gz','.tar.tgz','.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt','.git','.svn','.swp','.mdb','.old','.log']


def Name_url(url):
    ex = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
    name = re.search(ex, url, re.S)
    if url != 'None':
        name_list = name[0].split('.')
        name_url = name_list[-2] + '.' + name_list[-1]
        return name_url

# 生成特使特殊路径
def zj(urls_list):   # 生成特殊路径
    urls_dir = []
    txt_list = ['db','1','111','123']
    for url in urls_list:
        for txt in txt_list:
            url_bk = url + txt
            urls_dir.append(url_bk)
    return urls_list+urls_dir

#  分解url
def fuzzdir(url):
    global  file_txt_name
    urls=[]
    ex = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
    name = re.search(ex, url, re.S)
    if url != 'None':
        name_list = name[0].split('.')
        if len(name_list) == 2:  # 分解https://baidu.com
            name_url = name_list[-2] + '.' + name_list[-1]
            urls.append(name_list[0])
            urls.append(name_url)
            urls.append('www.'+name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append(name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append('www_'+name_url)
            urls = zj(urls)
            return urls
        elif len(name_list) == 3:   # 分解https://www.baidu.com 或 https://pan.baidu.com
            i = name_list.count('www')
            if i == 0:
                name_url = name_list[-2] + '.' + name_list[-1]
                urls.append(name_list[0])
                urls.append(name_list[1])
                urls.append(name_url)
                urls.append('www.' + name_url)
                name_url =  name_list[-3] + '.'+name_list[-2] + '.' + name_list[-1]
                urls.append(name_url)
                urls.append('www.' + name_url)
                name_url = name_list[-2] + '_' + name_list[-1]
                urls.append(name_url)
                name_url = name_list[-2] + '_' + name_list[-1]
                urls.append('www_' + name_url)
                name_url =  name_list[-3] + '_'+name_list[-2] + '_' + name_list[-1]
                urls.append(name_url)
                urls.append('www_' + name_url)
                urls = zj(urls)
                return urls
            else:
                if i != 0:
                    urls.append(name_list[1])
                    name_url = name_list[-2] + '.' + name_list[-1]
                    urls.append(name_url)
                    urls.append('www.' + name_url)
                    name_url = name_list[-2] + '_' + name_list[-1]
                    urls.append(name_url)
                    name_url = name_list[-2] + '_' + name_list[-1]
                    urls.append('www_' + name_url)
                    urls = zj(urls)
                    return urls
        elif len(name_list) == 4:  # 分解https://www.pan.baidu.com
            name_url = name_list[-2] + '.' + name_list[-1]
            urls.append(name_list[1])
            urls.append(name_list[2])
            urls.append(name_url)
            urls.append('www.' + name_url)
            name_url = name_list[-3] + '.' + name_list[-2] + '.' + name_list[-1]
            urls.append(name_url)
            urls.append('www.' + name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append(name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append('www_' + name_url)
            name_url = name_list[-3] + '_' + name_list[-2] + '_' + name_list[-1]
            urls.append(name_url)
            urls.append('www_' + name_url)
            urls = zj(urls)
            return urls

# 读取rar.txt 并生成 dirs
def flie_txt():
    dir_s = []
    i = 0
    module_name = os.path.abspath(os.path.dirname(__file__))[:-11]+"attackTools"
    with open(module_name+'/rar.txt', mode='r', encoding='UTF-8-sig') as fp:
        for dir_txt in fp:
            dir = dir_txt.rstrip()
            for hz in houzhui:
                url_dir_hz =  dir + hz
                zj(dir_s)
                dir_s.append(url_dir_hz)
                i += 1
        return dir_s

#　返回urls列表
def ret_list(url):
    if url[-1:] == "/":
        url = url[:-1]
    else:
        url = url
    url_list = fuzzdir(url)
    dir_s = flie_txt()
    for url_dir in url_list:
        for hz in houzhui:
            url_dir_hz = '/' + url_dir + hz
            dir_s.append(url_dir_hz)
    urls = []
    i = 0
    for dir_hz in dir_s:
        i +=1
        url_dic = {}
        url_dir = url + dir_hz
        url_dic.update({'url':url_dir})
        urls.append(url_dic)
    return urls

# 请求
def requ(url):
    url_200_list = []
    try:
        url_u = url['url']
        requests.packages.urllib3.disable_warnings()
        code = requests.head(url=url_u,headers=header[random.randint(0, len(header)-1)],verify=False,timeout=10)
        if code.status_code == 200 and int(code.headers['Content-Length']) > 1079705 :
            module_name = os.path.abspath(os.path.dirname(__file__))[:-11]
            with open(module_name+"backups.txt", mode='a+', encoding='UTF-8-sig') as fp:
                url_200_list.append(url_u)
                fp.write(url_u+'\n')
                print('==================可能存在备份文件==================')
                for url_200_list in url_200_list:
                    print(url_200_list)
    except Exception as a:
        pass

# 运行

def run(url):
    try:
        urls = ret_list(url)
        pool = Pool(100)
        pool.map(requ,urls)
        pool.close()
        pool.join()
    except Exception as a:
        print(a)


otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S")

i = -1
urls_txt = []

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


def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    try:
        run(url_)
    except Exception as e:
        print(f"{otherStyleTime }   {ts} ==> {url_} ==> Error")

def PocSuccess(success):
    with open('resuit.txt', mode='a+', encoding='UTF-8-sig') as fp:
        fp.write(success + "\n")


# 创建线程列表
def goRun(txt,T):
    otherStyleTime = time.strftime("%Y-%m-%d %H-%M-%S") + '.txt'
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
