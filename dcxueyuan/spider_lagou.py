#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
from pymongo import MongoClient
from fake_useragent import UserAgent

client = MongoClient()
db = client.lagou #链接test数据库 没有就自动创建
myset = db.job #使用set集合  没有就自动创建

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false&isSchoolJob=0'

def get_job_info(page, search):

    header = {
        'Cookie':'user_trace_token=20170506031712-70f66cf2-31c7-11e7-b71f-5254005c3644; LGUID=20170506031712-70f671e2-31c7-11e7-b71f-5254005c3644; JSESSIONID=ABAAABAACDBABJBBE9EFDA8E68F71839C7B397A695F3808; _gid=GA1.2.496802712.1516897481; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516897481; LGSID=20180126002441-3ed2a4d4-01ec-11e8-ab9d-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dk77SiTeh9HTA8PFZZYLfz1AyUZgR4U86o1xSsyjkfYW%26wd%3D%26eqid%3Dac5af9b00001aef0000000025a6a04be; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%B9%BF%E5%B7%9E; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516897594; LGRID=20180126002633-81c5cc49-01ec-11e8-ab9d-5254005c3644;',
        'Host':'www.lagou.com',
        'Origin':'https://www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?oquery=%E7%88%AC%E8%99%AB&fromSearch=true&labelWords=relative&city=%E5%B9%BF%E5%B7%9E',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    for i in range(page):
        payload = {
            'first':'true',
            'pn':i,
            'kd': search
        }

        ua = UserAgent()
        header['User-Agent'] = ua.random
        result = requests.post(url, data=payload, headers=header)
        if result.status_code == 200:
            job_json = result.json()['content']['positionResult']['result']
            myset.insert(job_json)
        else:
            print('Something wrong')
        time.sleep(3)
        print("now spidering "+ str(i+1) + 'page')
        #print(result['content']['positionResult']['result'])

if __name__ == '__main__':
    get_job_info(7, 'python爬虫')






