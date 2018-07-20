#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import math

import os

folder = './wx_avatar/'

# 获取所有图片
ls = os.listdir(folder)
# print(ls)

# sqrt返回平方根
# print(int(math.sqrt(float(640*640)/48)))
each_size = int(math.sqrt(float(640*640) / len(ls)))
lines = int(640 / each_size)
image = Image.new('RGB', (640, 640))
x = 0
y = 0
for i in range(0, len(ls)):

    try:
        img = Image.open(folder+ls[i])
    except IOError:
        print('Error')
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save('concat_all.jpg')
