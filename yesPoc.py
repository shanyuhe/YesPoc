# -*-codeing = utf-8 -*-
# @Time : {DATE}
# @Author : 一秋小叶　qq 2900180755
# @FIle ： {NAME}
# @Software : PyCharm
import argparse
import time
from  attackTools import runpoc
from  attackTools import gofzbk
from  attackTools import goadmin
from  attackTools import goLiveTest



def logo():
    print( """ 
__ __                        
 \ \ / /                        
  \ \_/ /__ ___ _ __ ___ ___
   \ / _ \/ __| '_ \ / _ \ / __|
    | | __/\__ \ |_) | (_) | （__
    |_|\___||___/ .__/ \___/ \___|
                |_|               
""")
    print("  Author   : 一秋小叶")
    print("  Email    : 2900180755@qq.com")
    print("  Github   : https://github.com/shanyuhe")
    time.sleep(3)

if __name__ == '__main__':
    logo()
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help='导入文本')
    parser.add_argument('-s', help='-s poc poc扫描 -s admin 后台探测 -s back 备份文件 -s test 存活测试')
    args = parser.parse_args()
    if (args.r != None and args.s =='poc'):
        runpoc.goRun(args.r,T=5)
    elif(args.r != None and args.s == 'admin'):
            goadmin.goRun(args.r, T=5)
    elif(args.r != None and args.s == 'back'):
            gofzbk.goRun(args.r, T=5)
    elif (args.r != None and args.s == 'test'):
            goLiveTest.goRun(args.r, T=5)







