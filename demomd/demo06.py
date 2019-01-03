#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import random
from urllib import request, parse

sms_url = 'http://61.129.57.20:7891/mt?'

# 返回 随机密码 默认10位
def random_pwd(len = 10, type = 1):

    if type==2 :
        chars = '0123456789'
    elif type== 3:
        chars = 'abcdefghijklmnopqrstuvwxyz'
    elif type== 4:
        chars = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
    elif type== 5:
        chars = 'abcdefghijklmnopqrstuvwxyzABDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    password = ''
    for i in range(0, len):
        password += random.choice(chars)

    return password

code = random_pwd(6,2)
content = " 【duoyu】 %s (手机绑定验证码)，请在20分钟内完成绑定。如非本人操作，请忽略。" % code
msg = {
    'dc':15,
    'sm':content,
    'da':13570274240,
    'un':700002,
    'pw':700002,
    'tf':3,
    'rf':2
}
data = parse.urlencode(msg)
sms_url = sms_url+data
print(sms_url)
req = requests.get(sms_url)
print(req.text)
exit()

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
ir = requests.get(url, timeout=15)
if ir.status_code == 200:
    iris = ir.content
    iris = iris.decode()
    open('iris.csv', 'w').write(iris)

#u = request.urlopen(url)
#localFile = open('iris.csv', 'w')
#localFile.write(u.read())
#localFile.close()