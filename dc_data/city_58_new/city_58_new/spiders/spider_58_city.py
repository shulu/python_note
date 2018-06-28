# -*- coding: utf-8 -*-
import scrapy


class Spider58CitySpider(scrapy.Spider):
    name = 'spider_58_city'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    def parse(self, response):
        pass
