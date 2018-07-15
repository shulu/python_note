# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import City58Item
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider

class City58TestSpider(RedisSpider):
    name = 'city58_test'
    allowed_domains = ['58.com']
    start_urls = ['http://bj.58.com/chuzu/']

    def parse(self, response):

        jpy = PyQuery(response.text)
        li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li')
        for it in li_list.items():
            a_tag = it('div.des > h2 > a')
            item = City58Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = it('div.listliright > div.money > b').text()
            yield item

        if not li_list:
            return

        pn = response.meta.get('pn', 1)
        pn += 1
        # response.meta['pn'] = pn
        if pn > 5:
            return
        req = response.follow(
            '/chuzu/pn{}/'.format(pn),
            callback=self.parse,
            meta={'pn':pn}
        )
        yield req

        # test_request1 = Request(
        #     'http://bj.58.com/chuzu/pn3',
        #     callback=self.parse,
        #     errback=self.error_back,
        #     headers={},
        #     cookies={},
        #     priority=10,
        # )
        #
        # test_request2 = Request(
        #     'http://58.com',
        #     callback=self.parse,
        #     errback=self.error_back,
        #     priority=10,
        #     meta={'dont_redirect':True}
        # )
        #
        # test_request3 = Request(
        #     'http://58.com',
        #     callback=self.parse,
        #     errback=self.error_back,
        #     priority=10,
        #     dont_filter=True,
        #     # meta={'dont_redirect': True}
        # )
        #
        # yield test_request1
        # yield test_request2
        # yield test_request3

    def error_back(self, e):

        _ = self
        print(e)
        print('我报错了')