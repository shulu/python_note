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

    id = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    num = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()

class JilupianVideoInfoItem(scrapy.Item):

    id = scrapy.Field()
    vsid = scrapy.Field()
    order = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()