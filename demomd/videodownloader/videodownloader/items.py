# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideodownloaderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JilupianItem(scrapy.Item):

    id = scrapy.Field()
    title = scrapy.Field()
    zimu = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
