#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'


import requests
from PyPDF2 import PdfFileReader, PdfFileWriter
import random
import urllib.parse
import hashlib

def create_sign(q, appid, salt, key):
    '''
    制造签名
    '''
    sign = str(appid) + str(q) + str(salt) + str(key)
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))
    return md5.hexdigest()


def create_url(q, url):
    '''
    根据参数构造query字典
    '''
    appid = 20180519000161884  # 填入你的 appid ，为int类型
    key = 'rOf6UwNhnrC3FxaLxNW_'  # 填入你的 key ，为str类型
    fro = 'auto'
    to = 'zh'
    salt = random.randint(32768, 65536)
    sign = create_sign(q, appid, salt, key)
    url = url+'?appid='+str(appid)+'&q='+urllib.parse.quote(q)+'&from='+str(fro)+'&to='+str(to)+'&salt='+str(salt)+'&sign='+str(sign)
    return url


def translate(q):
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    url = create_url(q, url)
    r = requests.get(url)
    txt = r.json()
    if txt.get('trans_result', -1) == -1:
        print('程序已经出错，请查看报错信息：\n{}'.format(txt))
        return '这一部分翻译错误\n'
    return txt['trans_result'][0]['dst']


def readPdf():

    output = PdfFileWriter()
    pdfile = PdfFileReader("./encrypt_pdf/18.pdf")
    # print the title of document1.pdf
    pages = pdfile.getNumPages()
    with open('demo.txt', 'a+', encoding='utf-8') as f:
        for page in range(0, pages):

            file = pdfile.getPage(page)
            page_txt = file.extractText()
            f.write(page_txt)


def translatedpdf():

    with open('demo.txt', 'rb', encoding='utf-8') as f:
        print(f)