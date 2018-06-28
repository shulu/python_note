#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import json
import math
from openpyxl import load_workbook

url = 'https://g.banggood.com/banggood/www/pipelines.json?scope=all&page=1&private_token=s64NyxXzb-Dreu9-4iM3'
#url = 'https://g.banggood.com/users/shulu/projects?private_token=s64NyxXzb-Dreu9-4iM3'
ret = requests.get(url)
data = json.loads(ret.text)

all_beta_commit = data['count']['all']
pages = math.ceil(all_beta_commit/20)
# print("pipeline_id | author |     author_email      |  push branch |  now status ")
print("pipeline_id |   author |  push branch |  now status ")
for pipe in data['pipelines']:
    pipeline_id = str(pipe['id'])
    author = pipe['commit']['author_name']
    author_email = pipe['commit']['author_email']
    commit_message = pipe['commit']['title']
    branch = 'unknow'
    if pipe['ref']['branch']:
        branch = pipe['ref']['name']
    pipeline_status = pipe['details']['status']['label']
    # print('    ' + pipeline_id + '  | ' + author + '  | ' + author_email + ' | ' + branch + ' | ' + pipeline_status)
    print('    ' + pipeline_id + '  |   ' + author + ' |   ' + branch + '    | ' + pipeline_status)

#https://www.cnblogs.com/sun-haiyu/p/7096423.html
#wb = load_workbook('pipelines.xlse')
#sheet = wb.get_sheet_by_name('Sheet')
#sheet['A1'] = 'Hello world!'
#print(sheet['A1'].value)