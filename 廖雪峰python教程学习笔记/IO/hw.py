# -*- coding: utf-8 -*-
import os

pwd = os.path.abspath('.')
print(pwd)

search = input('请输入你搜索的文件关键 :')

if (len(search) < 1):
    raise '请至少输入一个字符'
elif search == ' ':
    raise '请不要输入空格'


suit = []

def searchFile(curPath):
    for f in os.listdir(curPath):
        absPath = os.path.join(curPath,f)
        print(absPath)
        if os.path.isfile(absPath):
            if search in f:
                relativePath = absPath[len(pwd)+1:]
                print(relativePath)
        else:
            searchFile(absPath)

searchFile(pwd)