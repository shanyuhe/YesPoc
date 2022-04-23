# -*-codeing = utf-8 -*-
# @Time : 2022/4/22
# @Author : 一秋小叶　qq 2900180755
# @FIle ： UA
# @Software : PyCharm
import random


def ua():
    header = [
        'Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html',
        'Baiduspider-image+(+http://www.baidu.com/search/spider.htm)',
        'Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SCH-N719 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 YisouSpider/1.0.0 Mobile Safari/533.1',
        'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider(compatible;',
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko)Version/4.0 Mobile Safari/534.30; 360Spider',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 3 0 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        'Sosoimagespider+(+http://help.soso.com/soso-image-spider.htm)',
        'Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)',
        'Mozilla/5.0 (compatible; Bytespider; https://zhanzhang.toutiao.com/) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)',
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko)Version/4.0 Mobile Safari/534.30; 360Spider']
    i = random.randint(0,len(header)-1)
    user_agent = header[i]
    header = {}
    header['User-Agent'] = user_agent
    return header
