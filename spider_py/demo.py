# -*- coding: utf-8 -*-

from urllib import request, parse

acfun_html = ''

url = 'http://www.acfun.cn/'
file = 'acfun.html'
wp = request.urlopen(url)  #打开数据网页数据

content = wp.read()
fp = open(file, "wb")     #写入指定文件夹
fp.write(content)            #写入数据
fp.close()