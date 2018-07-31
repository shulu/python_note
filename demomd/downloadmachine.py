#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from subprocess import Popen, run, call
import requests
from lxml import etree

req = requests.get('http://open.163.com/special/opencourse/machinelearning.html')
#file = open('machinelearn.txt', 'w', encoding='utf-8')
#file.write(req.text)
#jp = PyQuery(req.text)
#items = jp('#list2 > tbody > tr').items()
#for it in items:
#    print(it)
xp = etree.HTML(req.text)
tr_list = xp.xpath('//*[@id="list2"]/tr')
dls = []
for i in range(2, len(tr_list)+1):
    dl_url = xp.xpath('//*[@id="list2"]/tr['+str(i)+']/td[1]/a/@href')[0]
    dls.append(dl_url)
    # call(['you-get', 'http://open.163.com/movie/2008/1/M/C/M6SGF6VB4_M6SGHFBMC.html'])

for dl_url in dls:
    # p = Popen('you-get -i {}'.format(dl_url), shell=True)
    p = Popen('you-get {}'.format(dl_url), shell=True)
    p.wait()
    # run(['you-get', '-i', dl_url])
    # call(['you-get', '-i', dl_url])