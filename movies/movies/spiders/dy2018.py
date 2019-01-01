# -*- coding: utf-8 -*-
import scrapy


class Dy2018Spider(scrapy.Spider):
    name = 'dy2018'
    allowed_domains = ['dy2018.com']
    #start_urls = ['https://dy2018.com/']
    host = 'https://www.dy2018.com/{}/'
    type_code = [x for x in range(0,21)]


    def start_requests(self):

        start_urls = [self.host.format(x) for x in self.type_code]
        print(start_urls)


    def parse(self, response):
        pass
