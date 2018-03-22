# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from ..items import City58Item

class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'
    allowed_domains = ['58.com']
    start_urls = ['http://gz.58.com/chuzu']

    def parse(self, response):
        print('我进入了解析器')
        # open('58.html', 'a',encoding='utf-8').write(response.text)
        jpy = pq(response.text)
        li_list = jpy("body > div.mainbox > div.main > div.content > div.listBox > ul > li").items()
        #print(li_list)
        for li in li_list:
            a_tag = li('div.des > h2 > a')
            item = City58Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = li('div.listliright > div.money > b').text()
            yield item
            #pass