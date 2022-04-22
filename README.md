
<p align="center"><img src="https://qlogo4.store.qq.com/qzone/2900180755/2900180755/100?1640892599"
        alt="Logo" width="158" height="82" style="max-width: 100%;"></p>
<h1 align="center">YesPoc</h1>
<p align="center">公众号：黑狗白狗都是好狗~</p>
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-3-blue.svg" alt="python3" />
    </a>
</p>
一个集和多线程,批量验证,poc验证,存活测试,备份文件探测,后台探测,渗透测试框架。

***本项目用来交流学习，切勿对未授权往网站进行扫描**
___

## -功能如下 
- [x] 多线程 + 协程
- [x] 批量验证
- [x] Poc检测，支持自定义POC
- [x] 备份文件扫描
- [x] 存活测试
- [x] 后台探测
- [ ] 更多功能待更新

___
**-安装**
```
# 下载安装
cd YesPOC
pip install -r requirement.txt 
```
**-使用**

```
python yesPoc.py -h
  -h, --help  show this help message and exit
  -r R        导入文本
  -s S        -s poc poc扫描 -s admin 后台探测 -s back 备份文件 -s test 存活测试
```

**-简单任务**
```
python yesPoc.py -u https://xxxx.com -poc 模块名称 # 使用指定模块扫描
python yesPoc.py -u https://xxxx.com -poc all      # 使用全部模块扫描
```
**-批量任务**
```
python yesPoc.py -r test.txt -s poc # poc扫描
python yesPoc.py -r test.txt -s admin # 后台探测
python yesPoc.py -r test.txt -s back # 备份文件
python yesPoc.py -r test.txt -s test # 存活测试
```
___
## -POC编写
  | 星期        | 车次           | 时间  |
| ------------- |:-------------:| -----:|
| 星期一      |G1008 | 4:30 |
|  星期二  | G1006      |  14:55 |
|  星期三   | G1007    |   18:30 |

___

## -POC编写
  poc简单例子[POC编写](https://github.com/saucer-man/saucerframe/wiki/poc%E7%BC%96%E5%86%99 "悬停显示")
___

## -感谢
  poc借鉴了[saucerframe](https://github.com/saucer-man/saucerframe "悬停显示")，特此说明和感谢。


