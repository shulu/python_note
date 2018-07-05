#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import numpy as np
import pandas as pd

# df = pd.DataFrame(pd.read_excel('pipelines.xlsx'))
df = pd.DataFrame(
    {
        "id":[1001, 1002, 1003, 1004, 1005, 1006],
        "date":pd.date_range('20130102', periods=6),
        "city":["Beijing", "SH", ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
        "age":[23,44, 54, 32, 34, 32],
        "category":['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
        "price":[1200, np.nan, 2133, 5433, np.nan, 4432]
    },
    columns=['id', 'date', 'city', 'category', 'age', 'price']
)

# 查看数据的维度
# print(df.shape)
# 查看数据表信息
# print(df.info())
# 查看数据表各列格式
# print(df.dtypes)
# df.isnull()
# 查看唯一值
# df['col'].unique()
# 查看数据表数值
# df.values()
# 查看列名称
# print(df.keys())
# 查看前几行数据
# print(df.head(3))
# 查看后几行数据
# print(df.tail(3))
# 删除数据表中含有空值的行
# df.dropna(how='any')
# 使用数字来填充数据表中的空值
# df['price'].fillna(df['price].mean())
# df.fillna(value=0)
# 清除空格
# df['city'] = df['city'].map(str.strip())
# 列大小写转换
# df['city'] = df['city'].str.lower()
# 更改数据格式
# df['price'].astype['int']
# 更改列名称
# df.rename(columns={'category': 'category-size'})
# 删除重复值
# df['city'].drop_duplicates() 保留第一位的
# df['city'].drop_duplicates(keep='last') 保留最后一个
# 数值的修改和替换
# df['city'].replace('sh', 'shanghai')


