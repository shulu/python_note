# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JilupianItem(scrapy.Item):

    id = scrapy.Field()
    title = scrapy.Field()
    zimu = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()


class JilupianInfoItem(scrapy.Item):

    pass