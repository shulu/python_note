#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import sys
import re
import urllib.request
import urllib
import http.cookiejar

from collections import deque


# 定义队列
queue = deque()
# 定义访问集合
visited = set()
# header
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': 1,
    'Host': 'video.yaodaojiao.com',
    'Referer': 'https://www.baidu.com/link?url=wpu8Nb5-dNwNy44d_9i_JpGrdg484LOR1aLoELZYOLUj7WxPCDfSufIvhOutsk_2&wd=&eqid=b330328b00003e270000000659dfce22',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, item in head.items():
        elem = (key, item)
        header.append(elem)
    opener.addheaders = header
    return opener

def saveFile(data):
    save_path = 'demo.md'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()

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
    urlop=urllib.request.urlopen(url, timeout=3)
    # print(urlop.getheader('Content-Type'))
    # 只读取html文件
    if 'html' not in urlop.getheader('Content-Type'):
        continue
    # 避免程序异常中止 用try..catch处理异常
    # response = urlop.info()
    # print(response)
    # data = urlop.read().decode('utf-8', 'ignore')
    # print(data)
    try:
        data = urlop.read().decode('utf-8', 'ignore')
        # print(data)
    except:
        print('read error')
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过 然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->    ' + x)
    # print(queue)