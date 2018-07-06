#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import pandas as pd
import numpy as np


df = pd.DataFrame(pd.read_excel('pipelines_bak.xlsx'))
#df = pd.DataFrame(pd.read_excel('pipelines.xlsx'))

# data = df.loc[df['author'].isin(['李俊波']), ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# data = df.loc[df['author']=='李俊波', ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# ['周海东' '余亚' '李俊波' '卢仕幸' '朱志明' '周佳献' '李阳阳' '严伟明' '杨智富' '邓永军' '杨水荣' '谢鼎杰' '陈首全']
author = '舒露'
author_pipelines = df.loc[df['author'] == author]
#first_commit = author_pipelines.iloc[[0]].commit_id.values[0]
first_commit = author_pipelines['commit_id'].head(1).values
#print(author_pipelines['commit_id'].tail(1).values)
#exit()
last_commit = author_pipelines['commit_id'].tail(1).values
used_branch_index = author_pipelines.groupby('branch')['pipeline_id'].count().index.values
used_branch_values = author_pipelines.groupby('branch')['pipeline_id'].count().values
print("now author: %s" % author)
print("author first commit: %s" % first_commit)
print("author last commit: %s" % last_commit)
for i in range(0, len(used_branch_index)):
    print('%s commit to branch %s %d times' % (author, used_branch_index[i], used_branch_values[i]) )
print('-----------------------------------------------------------')
exit()
authors = df['author'].unique()
for author in authors:

    first_commit = df.loc[df['author'] == author, ['commit_id']].iloc[[0]].commit_id.values[0]
    last_commit = df.loc[df['author'] == author, ['commit_id']].iloc[[-1]].commit_id.values[0]
    used_branch_index = author_pipelines.groupby('branch')['pipeline_id'].count().index.values
    used_branch_values = author_pipelines.groupby('branch')['pipeline_id'].count().values
    print("now author: %s" % author)
    print("author first commit: %s" % first_commit)
    print("author last commit: %s" % last_commit)
    for i in range(0, len(used_branch_index)):
        print('%s commit to branch %s %d times' % (author, used_branch_index[i], used_branch_values[i]) )
    print('-----------------------------------------------------------')
