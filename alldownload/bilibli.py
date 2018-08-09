#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from subprocess import Popen, run, call
import requests
from lxml import etree
import json
import random
import time

num_str = '1'
for i in range(1,20):
    num_str+=str(random.randint(0,9))

video_url = 'https://www.bilibili.com/bangumi/play/ep{}?from=search&seid={}'
req = requests.get('https://bangumi.bilibili.com/view/web_api/season?media_id=6360')
# file = open('demo.html', 'w', encoding='utf-8')
# file.write(req.text)
ret = json.loads(req.text)
# print(ret)
title = ret['result']['title']

for episode in ret['result']['episodes']:

    ep_id = episode['ep_id']
    index = episode['index']
    index_title = episode['index_title']
    dl_url = video_url.format(ep_id, num_str)
    print(dl_url)
    p = Popen('you-get -o ./{} -O {}-{} {}'.format(title, index, index_title, dl_url), shell=True)
    p.wait()
    time.sleep(30)

