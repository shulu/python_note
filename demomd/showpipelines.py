#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import json
import math
from openpyxl import load_workbook


class my_pipelines():

    def __init__(self):

        self.project = 'banggood/www'
        self.private_token = 's64NyxXzb-Dreu9-4iM3'
        self.excel_name = 'pipelines.xlsx'

    def get_pipelines(self):

        data = self.return_pipelines(False)
        all_commit = data['count']['all']
        self.record_max(all_commit)
        pages = int(math.ceil(all_commit/20))

        while pages > 0:
            print('start page '+str(pages))
            data = self.return_pipelines(pages)
            pipelines_data = []
            # pipeline_id	author	author_email	branch	commit_id	commit_message	commit_date pipeline_status
            for pipe in data['pipelines']:

                pipeline_id = str(pipe['id'])
                author = pipe['commit']['author_name']
                commit_id = pipe['commit']['id']
                commit_date = pipe['created_at']
                author_email = pipe['commit']['author_email']
                commit_message = pipe['commit']['title']
                branch = 'unknow'
                if pipe['ref']['branch']:
                    branch = pipe['ref']['name']
                pipeline_status = pipe['details']['status']['label']
                pipeline = [
                    pipeline_id, author, author_email, branch,
                    commit_id, commit_message, commit_date, pipeline_status
                ]
                pipelines_data.append(pipeline)
                # print('    ' + pipeline_id + '  |   ' + author + ' |   ' + branch + '    | ' + pipeline_status)
            self.save_to_excel(pipelines_data)
            pages -= 1

    def return_pipelines(self, page):

        if page:
            url = 'https://g.banggood.com/' + self.project + '/pipelines.json?scope=all&page='+str(page)+'&private_token=' + self.private_token
        else:
            url = 'https://g.banggood.com/' + self.project + '/pipelines.json?scope=all&page=1&private_token=' + self.private_token
        ret = requests.get(url)
        if ret.status_code == 200:
            data = json.loads(ret.text)
            return data
        else:
            return False

    def save_to_excel(self, datas):

        wb = load_workbook(self.excel_name)
        sheet = wb.active
        row = sheet.max_row  # <-最大行数
        max_row = row + 1
        lens = len(datas)
        for i in range(0, lens-1):
            for col in range(1, len(datas[i]) + 1):
                # print(max_row, col1)
                _ = sheet.cell(row=max_row, column=col, value=str(datas[i][col - 1]))
            max_row += 1
            wb.save(filename=self.excel_name)
        # print("保存成功")

    @staticmethod
    def record_max(count):
        with open("max_count.json", "w") as f:
            json.dump({'all_count':count}, f)
        print("加载入文件完成...")

if __name__ == '__main__':

    pipe = my_pipelines()
    pipe.get_pipelines()