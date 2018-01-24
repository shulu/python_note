# -*- coding: utf-8 -*-

import requests
import pandas as pd
import time

headers = {
    'authorization' : 'Bearer 2|1:0|10:1513516260|4:z_c0|92:Mi4xRVRzbUJRQUFBQUFBQU1MVjdHTk5DeVlBQUFCZ0FsVk41TG9qV3dEOGlOcWNyMkYxYk9wdHgyREkyTUtGenhmLXNB|f7205be6d57eec21afc705af5ce2e317fc882cd0da286dd402f018ebe801fc0f',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

user_data = []

def get_user_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        response = requests.get(url, headers=headers).json()['data']
        user_data.extend(response)
        print("正在爬取第%s页" % str(i+1))
        time.sleep(1)
        #print(response)

if __name__ == '__main__':
    get_user_data(10)
    df = pd.DataFrame.from_dict(user_data)
    #print(df)
    df.to_csv('users.csv')

