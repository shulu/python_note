#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
from pyquery import PyQuery

url = 'http://bj.58.com/chuzu/'

response = requests.get(url)
jpy = PyQuery(response.text)
li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li')
for it in li_list.items():
    a_tag = it('div.des > h2 > a')
    print(a_tag.text())