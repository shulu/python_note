#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
from requests.exceptions import RequestException
import json
import random

t = str(random.random())
market_url = 'https://ceo.bi/trade/index_json?t='+t
index_url = 'https://ceo.bi/'
print(index_url)
#exit()
header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'ceo.bi',
    'Origin': 'https://ceo.bi',
    'Referer': 'https://ceo.bi/t/cny_ltc.jsp',
    'Cookie': 'aliyungf_tc=AQAAADEAkkX3TwAASl4XDt1dnlQdkghx;JSPSESSID=n5nl88ugm6pqfkg2f7pl67n156;move_moble=13570274240; move_mobles=%2B86; title234=1;Hm_lvt_8ea3f9ee7328affe1c09a675ba5961a6=1525655827;Hm_lpvt_8ea3f9ee7328affe1c09a675ba5961a6=1525658317',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest'
}

try:
    # res = requests.post(url, headers=header, timeout=10, verify=True)
    res = requests.get(index_url)
    is_ok = res.status_code
    print(is_ok)
except RequestException as e:
    print('出现错误， 错误原因: ', e)
