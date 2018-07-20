#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
from lxml import etree

# https://www.kuaidaili.com/free/inha/1/
# //*[@id="list"]/table/tbody/tr[1]/td[1]
# //*[@id="list"]/table/tbody/tr[2]/td[1]

# 定义一个翻页函数，用来爬取“快代理”这个网站上的免费代理IP
def fanye(pages=1):
    ips = [] # IP和端口分别保存
    ports = []
    for i in range(pages):
        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(str(i+1))
        response = requests.get(url=url)
        parsed_text = etree.HTML(response.text)
        ip = parsed_text.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
        port = parsed_text.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
        ips.extend(ip)
        ports.extend(port)

    return ips, ports


ips_test, ports_test = fanye(pages=30) #这里调用了一下前面定义的函数，翻了2页

test_url = 'https://www.baidu.com/' #这只是一个用来测试的网址，可以修改为目标网站

print(ips_test)
print(ports_test)

proxies_pool = [] #初始化一个代理池列表

for ip_test in ips_test: #遍历一下爬取下来的IP列表
    port_test = ports_test[ips_test.index(ip_test)] #取出跟IP相对应的端口

    proxies = {
        'http': 'http://{}:{}'.format(ip_test,port_test),
        'https': 'http://{}:{}'.format(ip_test,port_test),
    }
    try: #异常处理
        response1 = requests.get(test_url, proxies=proxies, timeout=3)
        if response1.status_code == 200:
            proxies_pool.append({ip_test:port_test})
            print('代理IP{}已保存！'.format(ip_test))
        else:
            print('代理IP请求不成功！')
    except:
        print('代理IP无效！')

# 最后可用的IP数据
proxies_len = len(proxies_pool)
print('可用IP数目为{}，全部已保存！'.format(str(proxies_len)))