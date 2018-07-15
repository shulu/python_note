# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import CrawlSpider
from scrapy.http import Request
import re
import json
import pprint

class JdSpiderSpider(CrawlSpider):
    name = 'jd_spider'
    allowed_domains = ['jd.com']
    start_urls = ['http://m.jd.com/']

    rules = [
        Rule(LinkExtractor(allow=()),
        callback='parse_shop',
        follow=True
        )
    ]

    def parse_shop(self, response):

        ware_id_list = list()
        # 对链接使用正则表达式进行筛选
        url_group_shop = LinkExtractor(allow=(r'(http|https)://item.m.jd.com/product/\d+.html')).extract_links(response)
        # 定义抓取正则表达式的抓取规则
        re_get_id = re.compile(r'(http|https)://item.m.jd.com/product/(\d+).html')

        for url in url_group_shop:

            ware_id = re_get_id.search(url).group(2)
            ware_id_list.append(ware_id)

        for id in ware_id_list:
            """
                https://item.m.jd.com/ware/detail.json?wareId={}
                https://p.3.cn/prices/mgets?type=1&skuIds=J_{}
            """
            yield Request('https://item.m.jd.com/ware/detail.json?wareId={}'.format(id),
                          callback=self.detail_page,
                          meta={'id':id},
                          priority=5
                          )

    def detail_page(self, response):
        _ = self
        data = json.loads(response.text)

        yield Request('https://p.3.cn/prices/mgets?type=1&skuIds=J_{}'.format(response.meta['id']),
                      callback=self.get_price_page,
                      meta={
                          'id': response.meta['id'],
                          'data':data
                      },
                      priority=10
                      )

    def get_price_page(self, response):
        _ = self
        data = json.loads(response.text)
        detail_data = response.meta['data']
        ware_id = response.meta['id']

        item = {
            'detail': detail_data,
            'price': data,
            'ware_id': ware_id
        }

        pprint.pprint(item)

        yield item