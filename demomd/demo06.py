#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
from urllib import request

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