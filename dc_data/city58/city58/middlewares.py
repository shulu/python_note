#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from scrapy import signals
import random
import scrapy.downloadermiddlewares.retry

class UAMiddlware(object):

    ua_list = [
        # Chrome浏览器
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        # 百度爬虫
        'Mozilla/5.0 (compatible; Baiduspider/2.0; - +http://www.baidu.com/search/spider.html)',
        # IE9浏览器
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        # 谷歌爬虫
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        # 必应爬虫
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    ]

    def process_request(self, request, spider):

        ua = random.choices(self.ua_list)
        request.headers['User-Agent'] = ua
        print(request.url)
        print(request.headers['User-Agent'])

    def process_reponse(self, response, spider):

        return response

    def process_exception(self, exception, spider):

        pass