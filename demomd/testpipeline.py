#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import json
import time
import re
import os
import pandas as pd

df = pd.DataFrame(pd.read_excel('pipelines.xlsx'))
print(df['pipeline_id'].tail(1).values[0])
exit()
def conv_utc_time():
    patt = re.compile(r'\d*-\d*-\d*')
    dt = '2018-06-22T01:29:55.826Z'
    dates = re.search("(\d*-\d*-\d*)", dt).group()
    times = re.search("(\d*:\d*:\d*)", dt).group()
    dt = dates+' '+times
    #转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    timestamp += 8*3600
    #转换成localtime
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

    print(dt)

if os.path.exists('max_count.json'):

    data = open('max_count.json').read()
    data = json.loads(data)
    last_allacount = data['all_count']
else:

    last_allacount = 0
    with open("max_count.json", "w") as f:
        json.dump({'all_count': 0}, f)

url = 'https://g.banggood.com/banggood/www/pipelines.json?scope=all&page=1&private_token=s64NyxXzb-Dreu9-4iM3'
ret = requests.get(url)
data = json.loads(ret.text)
print(data['count_all'])
all_commit = data[ 'count' ][ 'all' ]

# pipeline_id	author	author_email	branch	commit_id	commit_message	commit_date pipeline_status
pipelines = data['pipelines']
pipelines.reverse()
for pipe in pipelines:

    print(pipe)
    pipeline_id = str(pipe['id'])
    author = pipe['user']['name']
    branch = author_email = commit_id = commit_message = 'unknow'
    if pipe['commit']:
        commit_id = pipe['commit']['id']
        author_email = pipe['commit']['author_email']
        commit_message = pipe['commit']['title']

    commit_date = pipe['created_at']
    if pipe['ref']['branch']:
        branch = pipe['ref']['name']
    pipeline_status = pipe['details']['status']['label']
    pipeline = [
        pipeline_id, author, author_email, branch,
        commit_id, commit_message, commit_date, pipeline_status
    ]
    # print('    ' + pipeline_id + '  |   ' + author + ' |   ' + branch + '    | ' + pipeline_status)
