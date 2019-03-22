#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'SarcasMe'

from selenium import webdriver

url = 'https://lcwslogpy.newyx.jiulingwan.com/duoyu/login/?serverId=39830&account=552300&pf_account=552300&time=1553173308&sign=6b78d8fcc063faa2b1781bb54255a834';
driver = webdriver.Chrome()
driver.get(url)
pass