#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from collections import deque

import requests
from bs4 import BeautifulSoup
import pymysql
import time

url = "http://video.yaodaojiao.com/jinguang/"
# 定义队列
queue = deque()
# 加入访问页
queue.append(url)
# 定义访问集合
visited = set()
# 计数
cnt = 0
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


def convertcoding(str, coding):
    return str.encode(coding).decode('gb2312', 'ignore')

def store(sql):
    # 打开数据库连接
    con = pymysql.connect(user="root", password="123", port=3306, host="127.0.0.1", db="awesome", charset="utf8")
    # con = pymysql.connect(user="www-data", password="www-data", port=3306, host="127.0.0.1", db="awesome", charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    # 获取自增id
    new_id = cur.lastrowid
    cur.close()
    con.close()
    return new_id

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
    response = requests.get(url, timeout=3, headers=header, allow_redirects=False)
    coding = response.encoding
    # 避免程序异常中止 用try..catch处理异常
    try:
        soup = BeautifulSoup(response.text, "html.parser")
    except:
        print('read error')
        continue
    # 正则表达式提取页面中所有队列, 并判断是否已经访问过 然后加入待爬队列
    lm_boxs = soup.findAll("div", {'class': 'lm_box'})
    list_left = soup.findAll("div", {'class': 'list_left'})
    if lm_boxs:
        for lm_box in lm_boxs:
            href = lm_box.find('a')
            link = href['href']
            if 'http' in link and link not in visited:
                queue.append(link)
                print('加入队列 --->    ' + link)
                # print(queue)
    elif list_left:
        list_title = soup.find("div",{'class':'t_left'}).text
        list_title = convertcoding(list_title, coding)
        post_time = soup.find("div",{'class':'t_right'}).text
        post_time = convertcoding(post_time, coding)
        add_time = time.time()
        data = (0, list_title, '#', post_time, add_time)
        sql = "INSERT INTO `jinguang` (pid, title ,title_url, post_time, add_time) VALUES ('%d', '%s', '%s', '%s', '%f')" % data
        ins_id = store(sql)
        c_boxs = soup.findAll('div', {'class':'c_box'})
        for c_box in c_boxs:
            href = c_box.find('a')
            post_time = c_box.find('span').text
            post_time = convertcoding(post_time, coding)
            title = href.text
            title = convertcoding(title, coding)
            link = href['href']
            add_time = time.time()
            data = (ins_id, title, link, post_time, add_time)
            sql = "INSERT INTO `jinguang` (pid, title ,title_url, post_time, add_time) VALUES ('%d', '%s', '%s', '%s', '%f')" % data
            store(sql)
            # if 'http' in link and link not in visited:
            #      queue.append(link)
            #      print('加入队列 --->    ' + link)
            #      # print(queue)