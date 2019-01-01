#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import json

login_url = 'http://www.acfun.cn/login.aspx'
session_url = 'http://www.acfun.cn/verification/captcha'


def start_get_ession():

    session = requests.session()
    return session

def get_cookies(session_):

    session_.get(login_url)
    get_session(session_)

def get_session(session_):

    session_.get(session_url)

def login(session_):

    headers = {
        'Host': 'www.acfun.cn',
        'Origin': 'http://www.acfun.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    data= {
        'username': 13570274240,
        'password': 'SHU1202LU'
    }
    response = session_.post(login_url, headers = headers, data=data)
    cookie_file = open('ac_cookie.json', 'w')
    cookie_file.write(json.dumps(response.cookies.get_dict()))
    # print(response.cookies.get_dict())

if __name__ == '__main__':

    session = start_get_ession()
    get_cookies(session)
    login(session)