#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import sys
import re
import urllib.request
import urllib

from collections import deque


# 定义队列
queue = deque()
# 定义访问集合
visited = set()
# 入口页
url = "http://video.yaodaojiao.com/jinguang/"
# 加入访问页
queue.append(url)
# 计数
cnt = 0
# 循环读取
while queue:
    # 拿出要读取url
    url = queue.popleft()
    # 插入已访问
    visited |= {url}  # 标记已访问

    print('已经抓取: ' + str(cnt) + '   正在抓取 <---   ' + url)
    # 访问一次 计数加一
    cnt += 1
    # 访问地址
    urlop=urllib.request.urlopen(url)
    # print(urlop.getheader('Content-Type'))
    # 只读取html文件
    if 'html' not in urlop.getheader('Content-Type'):
        continue
    # 避免程序异常中止 用try..catch处理异常
    response = urlop.info()
    print(response)
    data = urlop.read().decode('utf-8', 'ignore')
    print(data)
    try:
        data = urlop.read().decode('utf-8')
        print(data)
    except:
        print('read error')
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过 然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->    ' + x)