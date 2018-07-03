#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import numpy as np
import pandas as pd

df = pd.DataFrame(pd.read_excel('pipelines.xlsx'))
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
