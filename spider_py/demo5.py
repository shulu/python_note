#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import re
import requests
from bs4 import BeautifulSoup
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
    'DNT': '1',
    'Host': 'video.yaodaojiao.com',
    'Referer': 'https://www.baidu.com/link?url=wpu8Nb5-dNwNy44d_9i_JpGrdg484LOR1aLoELZYOLUj7WxPCDfSufIvhOutsk_2&wd=&eqid=b330328b00003e270000000659dfce22',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


response = requests.get("http://video.yaodaojiao.com/jinguang/", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

for lm_box in soup.findAll("div", {'class':'lm_box'}):
    span = lm_box.find("span")
    href = lm_box.find('a')
    print(span, href['href'])