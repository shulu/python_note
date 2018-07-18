# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class CctvSpider(scrapy.Spider):
    name = 'cctv'
    allowed_domains = ['cctv.com']
    host = 'jishi.cctv.com'
    url_format = 'http://{}/doc/shujubao/{}/index.json'
    code = [chr(x) for x in range(0x41, 0x5B)]
    # start_urls = ['http://jishi.cctv.com/doc/shujubao/{}/index.json']

    def start_requests(self):

        start_urls = [self.url_format.format(self.host, code) for code in self.code]
        self.logger.debug(start_urls)
        for url in start_urls:
            # 不写回调函数默认调用parse
            yield Request(url)

    def parse(self, response):

        pass
