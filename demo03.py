# -*- coding: utf-8 -*-
inputH = input('请输入你的身高:')
inputW = input('请输入你的体重:')
height = float(inputH)
weight = float(inputW)
def checkBmi(h,w):
    bmi = w/(h*h)
    if bmi <= 18.5:
        return 'bmi: %f 低于18.5：过轻' % bmi
    elif 18.5<bmi<=25:
        return 'bmi: %f 18.5-25：正常' % bmi
    elif 25<bmi<=28:
        return 'bmi: %f 25-28：过重' % bmi
    elif 28<bmi<=32:
        return 'bmi: %f 28-32：肥胖' % bmi
    elif bmi>32:
        return 'bmi: %f 高于32：严重肥胖' % bmi

print(checkBmi(height,weight))