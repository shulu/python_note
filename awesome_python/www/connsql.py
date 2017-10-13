#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import pymysql


def store(sql):
    # 打开数据库连接
    con = pymysql.connect(user="root", password="123", port=3306, host="192.168.217.131", db="awesome", charset="utf8")
    # con = pymysql.connect(user="www-data", password="www-data", port=3306, host="127.0.0.1", db="awesome", charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    # 获取自增id
    new_id = cur.lastrowid
    cur.close()
    con.close()
    return new_id