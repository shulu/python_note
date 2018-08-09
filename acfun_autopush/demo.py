#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


acfun = webdriver.Chrome()
acfun.get('http://www.acfun.cn/login/')

account_elem = acfun.find_element_by_id('ipt-account-login')
pwd_elem = acfun.find_element_by_id('ipt-pwd-login')
# btnlogin_elem = acfun.find_element_by_class_name('btn-login')

account_elem.send_keys('13570274240')
pwd_elem.send_keys('SHU1202LU')
pwd_elem.send_keys(Keys.ENTER)
print(acfun.page_source)