# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.exceptions import DropItem
from pymongo import MongoClient
from scrapy.conf import settings
from pymongo.errors import DuplicateKeyError
from traceback import format_exc
from .items import JilupianItem, JilupianInfoItem
import json


class testPipeline(object):

    def open_spider(self, spider):
        self.file = open('jilupian_info.txt', 'w', encoding='utf-8')
        print('==========open file=========')

    def process_item(self, item, spider):

        line = '{}\n'.format(json.dumps(dict(item)))
        self.file.write(line)
        return item


    def close_spider(self, spider):

        self.file.close()
        print('==============close file==========')


class JilupianPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # 提取出了mongodb配置
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_db=settings.get('MONGODB_DATABASE', 'items')
        )

    def open_spider(self, spider):

        _ = spider
        self.client = MongoClient(self.mongo_uri)  #连接数据库
        self.db = self.client[self.mongo_db]
        # 在表city58_info中建立索引，并保证索引的唯一性
        self.db['jilupian_info'].ensure_index('url', unique=True)
        # 在表city58_chuzu_info中建立索引，并保证索引的唯一性
        # self.db['jilupian_detail_info'].ensure_index('url', unique=True)

    def close_spider(self, spider):
        _ = spider
        self.client.close()  #关闭数据库

    def process_item(self, item, spider):
        try:
            # 判断是否是小区的item
            if isinstance(item, JilupianItem):
                # 通过id判断，有就更新，没有就插入
                self.db['jilupian_info'].update({'id': item['id']}, {'$set': item}, upsert=True)
            # 判断是否是小区出租信息的item
            elif isinstance(item, JilupianInfoItem):
                try:
                    # 通过url判断，有就更新，没有就插入
                    self.db['city58_chuzu_info'].update({'url': item['url']}, {'$set': item}, upsert=True)
                # 打印错误
                except Exception as e:
                    print(e)

        except DuplicateKeyError:
            # 唯一键冲突报错
            spider.logger.debug(' duplicate key error collection')
        except Exception as e:
            _ = e
            spider.logger.error(format_exc())
        return item
