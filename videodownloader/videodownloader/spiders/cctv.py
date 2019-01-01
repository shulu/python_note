# -*- coding: utf-8 -*-

from traceback import format_exc

import scrapy
import json, time
from scrapy.http import Request
from ..items import JilupianItem, JilupianInfoItem, JilupianVideoInfoItem
from ..utils.parse import parse, detail_parse

class CctvSpider(scrapy.Spider):

    name = 'cctv'
    allowed_domains = ['cctv.com']
    host = 'jishi.cctv.com'
    url_format = 'http://{}/doc/shujubao/{}/index.json'
    chr_code = [chr(x) for x in range(0x41, 0x5B)]
    start_urls = ['http://jishi.cctv.com/doc/shujubao/A/index.json']

    def start_requests(self):

        start_urls = [self.url_format.format(self.host, code) for code in self.chr_code]
        # start_urls = [ 'http://jishi.cctv.com/doc/shujubao/A/index.json' ]
        self.logger.debug(start_urls)
        for url in start_urls:
            # 不写回调函数默认调用parse
            yield Request(url)

    def parse(self, response):

        url_list, data = parse(response)

        for info in data:

            item = JilupianItem()
            item['id'] = info['url'].split('/')[6][:-6]
            item['title'] = info['title']
            item['zimu'] = info['zimu']
            item['url'] = info['url']
            item['date'] = int(time.time())

            yield item

        for url in url_list:

            yield Request(
                 url=url,
                 callback=self.detail_parse,
                 errback=self.error_back,
             )

    def detail_parse(self, response):

        detail = detail_parse(response)

        detail_info = detail['info']
        detail_video = detail['video']

        item = JilupianInfoItem()
        item['id'] = detail_info['vsid']
        item['title'] = detail_info['video_name']
        item['director'] = detail_info['director']
        item['num'] = detail_info['num']
        item['img'] = detail_info['image']
        item['url'] = detail_info['video_url']
        item['type'] = detail_info['video_type']
        item['desc'] = detail_info['video_desc']
        item['date'] = detail_info['video_date']

        yield item

        for video in detail_video:

            item = JilupianVideoInfoItem()
            item['id'] = video['vid']
            item['vsid'] = video['vsid']
            item['order'] = video['order']
            item['title'] = video['t']
            item['img'] = video['url']
            item['url'] = video['img']
            item['date'] = int(time.time())

            yield item


    def error_back(self, e):

        _ = e
        self.logger.error(format_exc())

