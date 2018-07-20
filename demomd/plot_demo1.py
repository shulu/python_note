#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'


import numpy as np
import matplotlib.pyplot as plt

#设置x轴范围
x=[0,1]
#设置y轴范围
y=[0,1]
#创建绘图对象
plt.figure()
#创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
#plt.figure(figsize=(8,4))
#在当前绘图对象进行绘图，两个参数是x、y轴的数据
plt.plot(x,y)
#在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
#plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
#设置x轴标签
plt.xlabel("time(s)")
#设置y轴标签
plt.ylabel("value(m)")
#设置标题
plt.title("A simple plot")
#图表的标题
plt.title("PyPlot First Example")
#Y轴的范围
plt.ylim(-1.2,1.2)
#显示图示
plt.legend()
#显示图
plt.show()
#保存图像
plt.savefig("easyplot.png")