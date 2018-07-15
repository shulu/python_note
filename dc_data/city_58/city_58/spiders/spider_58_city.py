# -*- coding: utf-8 -*-

from traceback import format_exc

import scrapy
from scrapy.http import Request
from ..utils.parse import parse, \
    xiaoqu_parse, \
    get_ershou_price_list, \
    chuzu_list_pag_get_detail_url, \
    get_chuzu_house_info
from ..items import City58XiaoQu, City58ChuZuInfo


class Spider58CitySpider(scrapy.Spider):
    name = 'spider_58_city'
    allowed_domains = ['58.com']
    # start_urls = ['http://58.com/']
    host = 'cd.58.com'
    xiaoqu_url_format = 'http://{}/xiaoqu/{}/'
    xiaoqu_code = list()
    xiaoqu_code.append(21611)

    def start_requests(self):

        start_urls = [self.xiaoqu_url_format.format(self.host, code) for code in self.xiaoqu_code]
        self.logger.debug(start_urls)
        for url in start_urls:
            # 不写回调函数默认调用parse
            yield Request(url)

    def parse(self, response):

        url_list = parse(response)

        for url in url_list:

            yield Request(
                url,
                callback=self.xiaoqu_detail_page,
                errback=self.error_back
            )

    def xiaoqu_detail_page(self, response):

        _ = self
        data = xiaoqu_parse(response)
        item = City58XiaoQu()
        item.update(data)
        item['id'] = response.url.split('/')[4]
        yield item

        # 二手房
        url = 'http://{}/xiaoqu/{}/ershoufang'.format(self.host, item['id'])
        yield Request(
            url,
            callback=self.ershoufang_list_page,
            errback=self.error_back,
            meta={'id': item['id']}
        )

        # 出租房
        url = 'http://{}/xiaoqu/{}/chuzu'.format(self.host, item[ 'id' ])
        yield Request(
            url,
            callback=self.chuzu_list_page,
            errback=self.error_back,
            meta={'id': item[ 'id' ]}
        )

    def ershoufang_list_page(self, response):

        _ = self
        price_list = get_ershou_price_list(response)
        yield {'id': response.meta['id'], 'price_list': price_list}

        # 翻页

    def chuzu_list_page(self, response):

        url_list = chuzu_list_pag_get_detail_url(response)

        for url in url_list:
            yield response.request.replace(url=url, callback=self.chuzu_detail_page)

        # 翻页

    def chuzu_detail_page(self, response):

        data = get_chuzu_house_info(response)
        item = City58ChuZuInfo()
        item.update(data)
        item['id'] = response.meta['id']
        item['url'] = response.url
        yield item

    def error_back(self, e):

        _ = e
        self.logger.error(format_exc())

