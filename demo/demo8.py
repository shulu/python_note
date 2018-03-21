#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import numpy as np
import matplotlib.pyplot as plt
import json


count_num = []
sum_num = []
with open('hash_record.json', 'r') as record:
    record = json.load(record)
    for item in record:
        count_num.append(item['count_num'])
        sum_num.append(item['sum_num'])


plt.plot(sum_num, sum_num)# use pylab to plot x and y
plt.show()# show the plot on the screen
