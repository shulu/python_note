# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient()
db = client.test #链接test数据库 没有就自动创建
my_set = db.set #使用set集合  没有就自动创建

my_set.insert({"name":"yyy", "age":18})