# -*-codeing = utf-8 -*-
# @Time : 2022/4/28
# @Author : 一秋小叶　qq 2900180755
# @FIle ： FileLen
# @Software : PyCharm

def filelen(file_):
    with open(file=file_,mode='r',encoding='utf-8')as fp:
        len_ =  len(fp.readlines())
        if len_ > 100:
            return 100
        elif len_ <= 100:
            return len_


if __name__ == '__main__':
    print(filelen('协议.txt'))