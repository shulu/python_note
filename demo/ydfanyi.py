#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import os

'''如果需要用户权限，可以使用requests.session()客户端，先登录获得cookies，然后再发送post请求。'''

'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):

    filesize = os.path.getsize(filePath)
    fsize = filesize / float(1024 * 1024)
    return round(fsize, 2)

file = 'demo.docx'

filesize = get_FileSize(file)

file_ext = file.split('.')[1]

print()

upload_url = 'http://fanyi.youdao.com/trandoc/doc/upload'
login_url = 'http://fanyi.youdao.com/login?method=login'

translate_url = 'http://fanyi.youdao.com/trandoc/doc/viewpage?doc=8A4DCED292CE49928E403A51F6164789&client=docserver&keyfrom=doctran&page=1&_=1525861475769'
# files = {'your_file': open(file, 'rb')}
files = {
    'your_file': (
        file,
        open(file, 'rb'),
    )
}
payload = {
    'from': 'en',
    'to': 'zh-CH',
    'type': file_ext,
    'filename': file,
    'client': 'docserver',
    'keyfrom': 'new-fanyiweb',
    'size': filesize
}
print(payload)

header = {
    'Connection': 'keep-alive',
    'Host': 'fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/?keyfrom=tegg.index',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': ''
              '_ntes_nnid=dce3592baac74924e14343f32e8ff54d,1500283203193; '
              '_ntes_nuid=dce3592baac74924e14343f32e8ff54d; '
              'mail_psc_fingerprint=c0199dcf5722241397c9d087189e1688; '
              'usertrack=c+xxClmnfNVIW0c4Aw0vAg==; '
              'vjuids=6b89b2a02.15fec2e1fb5.0.1c39188a46e1e;NTES_CMT_USER_INFO=11530256%7Cqq961085397%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F67704b6dc52f4b3cb9d0744e358fdc2b20170619155123.jpg%7Cfalse%7CcXE5NjEwODUzOTdAMTYzLmNvbQ%3D%3D; nts_mail_user=qq961085397@163.com:-1:1; '
              '_ngd_tid=6cWxle8nEBqeZTn1I8tJW4WuQYWR99%2BT; '
              'vjlast=1511495967.1524105003.21; '
              'vinfo_n_f_l_n3=3ef5ebc8056e2d14.1.4.1511495966654.1520997973457.1524105073629; '
              '__f_=1525224421188; '
              '__e_=1525313203321; '
              'starttime=; '
              'mail_login_way=normal; '
              'df=mail163_letter; NTES_SESS=UC6FW6vZp8A2IzoLVqBAyObDAv1_7J8HxmU8aP9AVYE4B9CJrlWBUJc42GwW27JrsVeVLJNmCUvgGQcxyiqGv_1c6F2XQmj9QVDImPNisR7S.l78AM1eXfsnsFCRhF2LXwIztnh9p1WOVmA_QmmSXarLk1N2VOjMLgypYfLw29ZpabDG.w0KYDd7uTpGQUaQ__KOiVVY7FzHr; S_INFO=1525861191|0|3&40##|qq961085397; P_INFO=qq961085397@163.com|1525861191|0|dict_hts|11&14|gud&1525851599&dict_hts#gud&440100#10#0#0|135240&0|dict_hts&youdaodict_client&easyread&mail163&note_client|qq961085397@163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}

# s = requests.Session()



r = requests.post(upload_url, headers=header, data=payload, files=files)

print(r.text)






