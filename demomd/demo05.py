#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
driver.get("https://www.wjx.top/jq/20422849.aspx")

room = driver.find_element_by_xpath('//*[@id="q1"]')
room.send_keys("732")
#print(driver.page_source)