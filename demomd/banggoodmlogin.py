#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import re
from lxml import etree
import json

login_url = 'https://m.banggood.com/index.php?com=login&t=login&c=api'

def start_get_session():

    session = requests.Session()
    return session

def get_base_cookie(session_):

    response = session_.get('https://m.banggood.com/login.html?pannel=signin', verify=False)
    s = etree.HTML(response.text)
    js_text = s.xpath('/html/body/script[2]/text()')
    # str = "var rand_code = '5b4c57cd8d273';"
    rand_code = re.findall(r'rand_code = \'(\w{13})\'', js_text[0])
    rand_code = rand_code[0]
    response = get_token(session_, rand_code)
    token = json.loads(response.text)['result']
    return rand_code, token

def get_token(session_, rand_code_):

    data = {
        'rand_code':rand_code_
    }
    response = session_.post('https://m.banggood.com/index.php?com=login&t=generateToken&c=api', data=data)
    return response

def login(session_, email_ = '', password_ = '', vcode_ = '', rcode_ = '', token_ = ''):

    data = {
        'email': email_,
        'password': password_,
        'verify_code': vcode_,
        'rand_code': rcode_,
        'is_remember': '1',
        'login_token': token_
    }
    response = session_.post(login_url, data=data)
    print(json.loads(response.text)['result'])

if __name__ == '__main__':

    session = start_get_session()
    rcode, token = get_base_cookie(session)
    email = input('请输入你的邮箱:')
    pwd = input('请输入你的密码:')
    login(session, email, pwd, '', rcode, token)
