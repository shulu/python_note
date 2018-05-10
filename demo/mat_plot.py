#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import matplotlib.pyplot as plt
import numpy as np

# simple draw
x = np.linspace(0,2*np.pi, 50)

plt.subplot(7, 1, 1) # （行，列，活跃区）
plt.plot(x, np.sin(x))


# multiple draw
plt.subplot(7, 1, 2) # （行，列，活跃区）
plt.plot(x, np.sin(x), x, np.sin(2*x))


# define self outlook
plt.subplot(7, 1, 3) # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r-o',
         x, np.cos(x), 'g--')

plt.subplot(7, 1, 4) # （行，列，活跃区）
y = np.sin(x)
plt.scatter(x,y)

plt.subplot(7, 1, 5) # （行，列，活跃区）
# 彩色映射散点图
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
colour = np.random.rand(1000)
plt.scatter(x, y, size, colour)
plt.colorbar()

plt.subplot(7, 1, 6) # （行，列，活跃区）
# 直方图
x = np.random.randn(1000)
plt.hist(x, 50)


plt.subplot(7, 1, 7) # （行，列，活跃区）
# 添加标题，坐标轴标记和图例
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend() # 展示图例
plt.xlabel('Rads') # 给 x 轴添加标签
plt.ylabel('Amplitude') # 给 y 轴添加标签
plt.title('Sin and Cos Waves') # 添加图形标题
plt.show()
