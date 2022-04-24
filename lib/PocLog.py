# -*-codeing = utf-8 -*-
# @Time : {DATE}
# @Author : 一秋小叶　qq 2900180755
# @FIle ： {NAME}
# @Software : PyCharm
import time

def PocSuccess(file,success):
    with open(file, mode='a', encoding='UTF-8-sig') as fp:
        fp.write(success + "\n")
if __name__ == '__main__':
    print()

