#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
from subprocess import Popen
import json

webm = []
session_url = 'https://www.dcxueyuan.com/login.html'
login_url = 'https://www.dcxueyuan.com/user/common/login.json'
index_url = 'https://www.dcxueyuan.com/index.html'



def start_get_ession():

    session = requests.session()
    return session


def get_cookies(session_):

    header = {
        'Host': 'www.dcxueyuan.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    session_.get(session_url, headers=header)


def login(session_):

    headers = {
        'Host': 'www.dcxueyuan.com',
        'Origin': 'https://www.dcxueyuan.com',
        'Referer': 'https://www.dcxueyuan.com/login.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    data= {
        'username': '*****',
        'password': '*****'
    }
    response = session_.post(login_url, headers = headers, data=data)
    # get_cookies(session_)
    # print(response.text)
    pass


def get_session(session_):

    headers = {
        'Host': 'www.dcxueyuan.com',
        'Referer': 'https://www.dcxueyuan.com/login.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    requests.utils.add_dict_to_cookiejar(session_.cookies, {"_dcU": "*****"})
    session_.get(session_url, headers=headers)


def get_course(session_):
    course_url = 'https://www.dcxueyuan.com/user/getVideoUrl.json?classId={}&pixel=1080P&videoFrom=2'
    for i in range(51, 71):
    # for i in range(1, 36):
        res = session_.get(course_url.format(i))
        info = json.loads(res.text)
        # print(info)
        title = info['data']['class']['name']
        # video_url = info['data']['urls'][2]
        video_url = info['data']['url']
        webm.append([title, video_url])


def download_course():

    counts = 1
    for title,url in webm:
        p = Popen('you-get -o ./dc_video/webm -O {}-{} {}'.format(counts, title, url), shell=True)
        p.wait()
        counts+=1

if __name__ == '__main__':

    session = start_get_ession()
    get_cookies(session)
    login(session)
    get_session(session)
    get_course(session)
    print(webm)
    download_course()