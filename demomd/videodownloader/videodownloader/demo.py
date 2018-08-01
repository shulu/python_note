#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from subprocess import run, call, Popen
import requests
from lxml import etree
from pyquery import PyQuery
import re
import json

"""
    # tv.cctv.com
    //*[@id="page_body"]/div[7]/div/div[1]/div/img -image
    //*[@id="page_body"]/div[7]/div/div[2]/div/h3 -title
    //*[@id="page_body"]/div[7]/div/div[2]/div/p[1] -type
    //*[@id="page_body"]/div[7]/div/div[2]/div/p[2] -num
    //*[@id="page_body"]/div[7]/div/div[2]/div/p[3] -director
    //*[@id="zhankai"] -description
    //*[@id="fpy_ind04"]/dd[2] -video list
    # jishi.cctv.com
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/div/img -image
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td[2]/a -title
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[2]/td[2]/a -type
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[4]/td[2] -director
    //*[@id="foldtext"]/text() -description
    //*[@id="ypdianbo"]/div/ul/li/div[1]/a[1] -url
    :param response:
    :return:
    """
url = 'http://tv.cctv.com/2017/07/04/VIDESiZ5OCY9hwSwF7SY7fiA170704.shtml'
print(re.findall(r'(VIDE[\w]*)', url))
exit()
url1 = 'http://tv.cctv.com/2012/12/15/VIDA1355568145639422.shtml'
url2 = 'http://jishi.cctv.com/2016/09/12/VIDAV12WqaPzU09IZWj2WgsK160912.shtml'
rq = requests.get(url2)
# print(rq.encoding)
xp = etree.HTML(rq.text)
# file = open('jishi.txt', 'w', encoding='utf-8')
# file.write(rq.text.encode('ISO-8859-1').decode('utf-8'))
# jp = PyQuery(rq.text)

items = xp.xpath('//script/text()')
param = re.findall(r'(VSET[\d]{12})',items[12])[0]
dl_url = 'http://tv.cntv.cn/api/video/getvideo/vsid_{}'.format(param)
dl_rq = requests.get(dl_url)
video_info = json.loads(dl_rq.text)
vsid = video_info['videoset']['0']['vsid']
image = video_info['videoset']['0']['img']
num = video_info['videoset']['count']
video_url = video_info['videoset']['0']['url']
video_name = video_info['videoset']['0']['name']
video_date = video_info['videoset']['0']['nf']
video_type = video_info['videoset']['0']['fl']
video_desc = video_info['videoset']['0']['desc']
print(video_name+' : '+video_url)
# print(video_info)
for info in video_info['video']:
    print(info)
# count = 1
# for it in items:
#
#     piece__href = it.encode('ISO-8859-1').decode('utf-8')
#     print("index: {} href: {}".format(count, piece__href))
#     count+=1
#xp.xpath('//*[@id="page_body"]/div[7]/div/div[1]/div/img/@src')[0]
#xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/h3/text()')[0].encode('ISO-8859-1').decode('utf-8')
#xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[1]/span')[0].tail.encode('ISO-8859-1').decode('utf-8')
#xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[2]')[0].tail.encode('ISO-8859-1').decode('utf-8')
#xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[3]')[0].tail.encode('ISO-8859-1').decode('utf-8')
#items = xp.xpath('//*[@id="fpy_ind04"]/dd')
#for it in range(1, len(items)):
    # piece__href = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[1]/@href'.format(it))[0]
    # piece_title = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[1]/@title'.format(it))[0].encode('ISO-8859-1').decode('utf-8')
    # print("href: {} title: {}".format(piece__href, piece_title))
#xp.xpath('//*[@id="shuoqi"]/span')[0].tail.encode('ISO-8859-1').decode('utf-8')

pass