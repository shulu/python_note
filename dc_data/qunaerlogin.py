#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import re

url = 'https://user.qunar.com/passport/loginx.jsp'
img_url = 'https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a'
ick_url = 'https://user.qunar.com/passport/addICK.jsp?ssl'
session_url = 'https://rmcsdf.qunar.com/js/df.js?org_id=ucenter.login&js_type=0'
fid_url = 'https://rmcsdf.qunar.com/api/device/challenge.json?callback=callback_1531636165377&sessionId={}&domain=qunar.com&orgId=ucenter.login'


def start_get_session():

    session = requests.session()
    return session

def get_base_cookies(session_):

    response = session_.get(url)
    get_image(session_)
    session_.get(ick_url)
    # 获取sessionId
    response = session_.get(session_url)
    session_id = re.findall(r'sessionId=(.*?)&', response.text)
    session_id = session_id[0]
    # 获取fid
    session_.get(fid_url.format(session_id))

    session_.cookies.update({'Qn271':session_id})

def get_image(session_):

    response = session_.get(img_url)
    # 图片存储是byte 因此是WB
    with open('code.png', 'wb') as f:
        # content保存有byte数据
        f.write(response.content)


def login(session_, uname_, pwd_, code_):

    data = {
        "loginType": 0,
        "ret": "https: // www.qunar.com /",
        "username": uname_,
        "password": pwd_,
        "remember": 1,
        "vcode": code_
    }

    response = session_.post(url, data=data)
    print(response.text)


if __name__ == '__main__':

    session = start_get_session()
    get_base_cookies(session)
    username = input("input uname: ")
    password = input('input password: ')
    code = input('input code:')

    login(session, username, password, code)