#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import pandas as pd
import numpy as np


df = pd.DataFrame(pd.read_excel('pipelines_bak.xlsx'))

# data = df.loc[df['author'].isin(['李俊波']), ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# data = df.loc[df['author']=='李俊波', ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# ['周海东' '余亚' '李俊波' '卢仕幸' '朱志明' '周佳献' '李阳阳' '严伟明' '杨智富' '邓永军' '杨水荣' '谢鼎杰' '陈首全']
author = '吴明聪'
first_commit = df.loc[df['author'] == author, ['commit_id']].iloc[[0]].commit_id.values[0]
last_commit = df.loc[df['author'] == author, ['commit_id']].iloc[[-1]].commit_id.values[0]
used_branch = df.loc[df['author'] == author, ['branch']].drop_duplicates().branch.values
count_branch = df.loc[df['author'] == author, ['branch', 'pipeline_id']].groupby('branch')['pipeline_id'].count().values
print("now author: %s" % author)
print("author first commit: %s" % first_commit)
print("author last commit: %s" % last_commit)
for i in range(0, len(used_branch)):
    print('%s commit to branch %s %d times' % (author, used_branch[i], count_branch[i]) )
print('-----------------------------------------------------------')
exit()
authors = df['author'].unique()
for author in authors:

    first_commit = df.loc[df['author'] == author, ['commit_id']].iloc[[0]].commit_id.values[0]
    last_commit = df.loc[df['author'] == author, ['commit_id']].iloc[[-1]].commit_id.values[0]
    used_branch = df.loc[df['author'] == author, ['branch']].drop_duplicates().branch.values
    count_branch = df.loc[df['author'] == author, ['branch', 'pipeline_id']].groupby('branch')['pipeline_id'].count().values
    print("now author: %s" % author)
    print("author first commit: %s" % first_commit)
    print("author last commit: %s" % last_commit)
    for i in range(0, len(used_branch)):
        print('%s commit to branch %s %d times' % (author, used_branch[i], count_branch[i]) )
    print('-----------------------------------------------------------')
