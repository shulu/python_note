#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import pandas as pd
import numpy as np


df = pd.DataFrame(pd.read_excel('pipelines.xlsx'))

# data = df.loc[df['author'].isin(['李俊波']), ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
# data = df.loc[df['author']=='李俊波', ['pipeline_id', 'author', 'commit_date']].pipeline_id.count()
authors = df['author'].unique()
for author in authors:

    first_commit = df.loc[df['author']==author, ['commit_id']].iloc[[0]].commit_id
    last_commit = df.loc[df['author']==author, ['commit_id']].iloc[[-1]].commit_id
    print(first_commit)
    print(last_commit)
    print("now author: %s" % author)
    print("author first commit:")
