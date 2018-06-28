#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import pandas as pd
import numpy as np

#print(np.random.randint(low=0, high=10, size=(5, 5)))

writer = pd.ExcelWriter('pipelines.xlsx')

df = pd.DataFrame([[1,2,3,4,5,6,7]], columns=['pipeline_id', 'author', 'author_email', 'commit_id', 'commit_message', 'branch', 'pipeline_status'])

#print(df)
df.to_excel(writer,'Sheet1')
writer.save()
