#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from numpy import genfromtxt, zeros
from matplotlib import pyplot

# read the first 4 columns
data = genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

print( data.shape)

print(target.shape)

# build a collection of unique elements
print(set(target))

pyplot.plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
pyplot.plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
pyplot.plot(data[target=='virginica',0],data[target=='virginica',2],'go')
pyplot.show()