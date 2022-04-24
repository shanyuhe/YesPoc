
<p align="center"><img src="https://qlogo4.store.qq.com/qzone/2900180755/2900180755/100?1640892599"
        alt="Logo" width="158" height="82" style="max-width: 100%;"></p>
<h1 align="center">YesPoc</h1>
<p align="center">Q   Q：2900180755~</p>
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
- [x] 单个任务
- [x] 批量验证
- [x] 备份文件扫描
- [x] 存活测试
- [x] 后台探测
- [x] Poc检测，支持自定义POC
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
  -u          指定url
  -poc        配合-u使用 -poc 模块名称 单个扫描 -poc all 使用全部模块进行扫描
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
## -更新日志
| Module name        | Update time          |              
| ------------- |:-------------|
| Apache-Flink-Web-Dashboard-RCE      |  -  |
| coremail_source_leak      |  -  | 
| couchdb_unauth      |  -  | 
| csbrute      |  -  | 
| cve-2020-0796      |  -  | 
| cve-2020-1938      |  -  | 
| CVE-2020-5902      |  -  | 
| CVE-2020-8813      |  -  | 
| CVE-2021-22986      |  -  | 
| CVE-2021-26084      |  -  | 
| CVE-2021-26855      |  -  | 
| CVE-2021-34473      |  -  | 
| dahua      |  -  | 
| discuz_rce      |  -  | 
| eyou      |  -  | 
| fastadmin_weak      |  -  | 
| fw_oa_rce      |  -  | 
| fw_sql      |  -  | 
| genkins_unauth      |  -  | 
| hbgk      |  -  | 
| hikvision      |  -  | 
| juanvision      |  -  | 
| mongodb_unauth      |  -  | 
| phpstudy_backdoor      |  -  | 
| redis_unauth      |  -  | 
| seeyon      |  -  | 
| test      |  -  | 
| thinkcmf_shell      |  -  | 
| thinkphp_rce      |  -  | 
| tongda_rce      |  -  | 
| vmware-vcenter      |  -  | 
| weblogic_2019_48814      |  -  | 
| weblogic_ssrf      |  -  | 
| weblogic_weak_pass      |  -  | 
| weblogic_xmldecoder_exec      |  -  | 
| wp_social_warfare_rce      |  -  | 
| yapi_rce      |  -  | 
| laraverDeBug      |  2022/04/22  | 
| env泄露      |  2022/04/22  | 
| git信息泄露      |  2022/04/22  | 
| CVE-2020-17519      |  2022/04/22  | 
| cve-2018-6910      |  2022/04/22  | 
| elasticsearch-unauth      |  2022/04/22  | 
|Hanming-Video-Conferencing    |  2022/04/22  | 
|cve-2018-12613    |  2022/04/22  |
|cve-2017-9841    |  2022/04/22  |
|cve-2020-5405    |  2022/04/22  |
|springboot-env    |  2022/04/22  |
|cve-2019-3799    |  2022/04/22  |
|cve-2020-5284    |  2022/04/22  |
|alibaba-nacos    |  2022/04/22  |

___

## -POC编写
  poc简单例子[POC编写](https://github.com/saucer-man/saucerframe/wiki/poc%E7%BC%96%E5%86%99 "悬停显示")
___

## -感谢
  poc借鉴了[saucerframe](https://github.com/saucer-man/saucerframe "悬停显示")，特此说明和感谢。


