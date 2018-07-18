# -*- coding: utf-8 -*-

from traceback import format_exc

import scrapy
import json, time
from scrapy.http import Request
from ..items import JilupianItem
from ..utils.parse import parse, detail_parse

class CctvSpider(scrapy.Spider):

    name = 'cctv'
    allowed_domains = ['cctv.com']
    host = 'jishi.cctv.com'
    url_format = 'http://{}/doc/shujubao/{}/index.json'
    chr_code = [chr(x) for x in range(0x41, 0x5B)]
    # start_urls = ['http://jishi.cctv.com/doc/shujubao/{}/index.json']

    def start_requests(self):

        start_urls = [self.url_format.format(self.host, code) for code in self.chr_code]
        self.logger.debug(start_urls)
        for url in start_urls:
            # 不写回调函数默认调用parse
            yield Request(url)

    def parse(self, response):

        url_list, data = parse(response)

        for info in data:

            item = JilupianItem()
            # item['id'] = info['url'].split['/'][6][-6]
            item[ 'title' ] = info[ 'title' ]
            item[ 'zimu' ] = info[ 'zimu' ]
            item[ 'url' ] = info[ 'url' ]
            item[ 'date' ] = int(time.time())

            yield item

        # for url in url_list:
        #
        #     yield Request(
        #         url=url,
        #         callback=self.detail_parse,
        #         errback=self.error_back,
        #     )


    def detail_parse(self, response):

        data = detail_parse(response)

        pass


    def error_back(self, e):

        _ = e
        self.logger.error(format_exc())

