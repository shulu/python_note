#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from scrapy import Selector
from pyquery import PyQuery

with open('index.html', encoding='utf-8') as f:
    text = f.read()

sel = Selector(text=text)
jpy = PyQuery(text)
items = jpy('li')
for item in items.items():
    print(item.attr('class'))
pass