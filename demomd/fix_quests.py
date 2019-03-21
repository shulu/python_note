#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
print(browser.page_source)
browser.close()