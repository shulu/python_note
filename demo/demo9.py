#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from pyecharts import Pie

attr = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']

v1 = [11,12,13,10,10,10]
v2 = [19,21,32,20,20,33]

pie = Pie('饼图-玫瑰图示意', title_pos='center', width=900)
pie.add('商品A', attr, v1, center=[27,75], is_random=True, radius=[30,75], rosetype='radius')

pie.render('demopie.html')