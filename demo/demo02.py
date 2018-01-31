#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from urllib import request
import time

url = 'https://www.banggood.com/SanQi-Elan-Squishy-Ice-Cream-Cone-Jumbo-22cm-Slow-Rising-With-Packaging-Collection-Gift-Soft-Toy-p-1179253.html?rmmds=detail-top-buytogether-auto__1&cur_warehouse=CN'

img_small_link = 'https://img1.banggood.com/thumb/other_items/oaupload/banggood/images/C8/DE/05153bbf-28cb-497f-9f36-8d892d36e507.jpg'
img_big_link = 'https://img3.banggood.com/thumb/large/oaupload/banggood/images/C8/DE/05153bbf-28cb-497f-9f36-8d892d36e507.jpg'
origin_html = requests.get(url).text

#soup = BeautifulSoup(origin_html, 'html.parser')
#img_div = soup.find('div', class_="good_photo_min")

s = etree.HTML(origin_html)
links = s.xpath('//a[contains(@big,"http")]')
big_img_list = []
for index in range(len(links)):
    big_img_list.append(links[index].attrib['big'])

#print(big_img_list)
for i in range(len(big_img_list)):
    f = open(str(i+1)+'.jpg',"wb")    #打开文件
    req = request.urlopen(big_img_list[i], timeout=10)
    buf = req.read()              #读出文件
    f.write(buf)                  #写入文件
    print("now writing "+ str(i+1) + '.jpg')
    time.sleep(1)

#f = open("demo02.html",'w', encoding='utf-8')
#f.write(origin_html)
#f.close()