#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import pandas as pd
import numpy as np
import calendar as cal

cals = []
year = 2017
for m in range(1, 13):
    d = cal.monthrange(year, m)
    #first_day = str(year)+'-'+str(m)+'-1'
    first_day = "%d-%d-%d" % (year, m, 1)
    last_day = "%d-%d-%d" % (year, m, d[1])
    # print("%d-%d-%d\t%d-%d-%d" % (year, m, 1, year, m, d[1]))
    cals.append([first_day, last_day])

df = pd.DataFrame(pd.read_excel('pipelines_bak.xlsx'))
#df = pd.DataFrame(pd.read_excel('pipelines.xlsx'))

# data = df.loc[df['author'].isin(['李俊波']), ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# data = df.loc[df['author']=='李俊波', ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# ['周海东' '余亚' '李俊波' '卢仕幸' '朱志明' '周佳献' '李阳阳' '严伟明' '杨智富' '邓永军' '杨水荣' '谢鼎杰' '陈首全']
author = '舒露'
print("now author: %s" % author)
author_pipelines = df.loc[df['author'] == author]
# first_commit = author_pipelines.iloc[[0]].commit_id.values[0]
# first_commit = author_pipelines['commit_id'].head(1).values
# first = author_pipelines.head(1)
# first_commit_date = str(first['commit_date'].values[0])
# first_commit_id = first['commit_id'].values[0]
# print("第一次提交日期为: %s 提交的commit_id: %s" % (first_commit_date, first_commit_id))
# last = author_pipelines.tail(1)
# last_commit_date = str(last['commit_date'].values[0])
# last_commit_id = str(last['commit_id'].values[0])
# print("最后一次提交日期为: %s 提交的commit_id: %s" % (last_commit_date, last_commit_id))
# #last_commit = author_pipelines['commit_id'].tail(1).values
# used_branch_index = author_pipelines.groupby('branch')['pipeline_id'].count().index.values
# print('-----------------------详细信息--------------------------------')
# print("常用分支： "+used_branch_index)
# used_branch_values = author_pipelines.groupby('branch')['pipeline_id'].count().values
# for i in range(0, len(used_branch_index)):
#     print('commit to branch %s %d times' % (used_branch_index[i], used_branch_values[i]) )
print('-----------------------年份提交信息--------------------------------')
# 设置日期为索引
author_pipelines['commit_date'].astype('str')
author_pipelines = author_pipelines.set_index('commit_date')
# 提取2017数据所有数据
month_count = []
for months in cals:
    month_data = author_pipelines[months[0]:months[1]]
    print(month_data.size)

