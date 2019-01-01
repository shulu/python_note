#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

index_url = 'http://www.acfun.cn'
login_url = 'http://www.acfun.cn/login/'
video_url = 'http://www.acfun.cn/member/#area=upload-video'
acfun = webdriver.Chrome()
# 初次建立连接，随后方可修改cookie
acfun.get(index_url)
# 删除第一次建立连接时的cookie
acfun.delete_all_cookies()
# 读取登录时存储到本地的cookie
with open('ac_cookie.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())

for cookie in listCookies:

    acfun.add_cookie({
        'domain': '.acfun.cn',  # 此处xxx.com前，需要带点
        'name': cookie,
        'value': listCookies[cookie],
        'path': '/',
        'expires': None
    })

# print(acfun.get_cookies())
# 再次访问页面，便可实现免登陆访问
acfun.refresh()
acfun.get(video_url)

title_elem = acfun.find_element_by_id('title')

#pwd_elem = acfun.find_element_by_name('channel')
#btnlogin_elem = acfun.find_element_by_class_name('btn-login')
up_pic = acfun.find_element_by_id('up-pic')
up_pic.click()
# account_elem.send_keys('13570274240')
# pwd_elem.send_keys('SHU1202LU')
# pwd_elem.send_keys(Keys.ENTER)
