#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrhSearch(unittest.TestCase):

    def set_up(self):

        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):

        driver = self.driver
        driver.get('http://www.python.org/')
        assert "Python" in driver.title
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert "No Results found." not in driver.page_source

    def tearDown(self):

        self.driver.close()

if __name__ == "__main__":

    unittest.main()

