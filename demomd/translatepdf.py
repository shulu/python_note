#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import hashlib
import random
import urllib.parse
import requests
from concurrent import futures
from io import StringIO
from subprocess import call
import chardet
from pathlib import Path
import filetype
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


file = r'./encrypt_pdf/18.pdf'
not_allowed_pdf = r'./encrypt_pdf/'
allowed_filetype = ['pdf', 'jpg', 'png']
#call('qpdf --password=%s --decrypt %s %s' % ('', file,  not_allowed_pdf+file), shell=True)
#exit()
def get_filetype(file):
    kind = filetype.guess(file)
    if kind is None:
        print('Cannot guess file type!')
        return
    return kind.extension
    # print('File extension: %s' % kind.extension)
    # print('File MIME type: %s' % kind.mime)

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


def parse(path):
    fp = open(path, 'rb')  # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        #call('qpdf --password=%s --decrypt %s %s' % ('', path,  not_allowed_pdf+path), shell=True)

        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            """
            这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure,
            LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性
            """
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    with open(r'demo.txt', 'a', encoding='utf-8') as f:
                        results = x.get_text()
                        translate_result = translate(results)
                        print(results +' '+ translate_result + ' ')
                        f.write(results + '  '+translate_result+'\n')


if  Path(file).exists():

    file_type = get_filetype(file)
    if file_type in allowed_filetype:

        if file_type == 'pdf' :
            parse(file)
        print(file+' is exists and allowed')
else:
    print(file+' is not exists')

