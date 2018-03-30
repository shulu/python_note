#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import os
import cv2

convert_path = './convert_img'

def checkConvert(path):
    files = os.listdir(path)
    for file in files:
        file_dir = path+'/'+file
        if os.path.isdir(file_dir):
            # print('is dir')
            checkConvert(file_dir)
        else:
            convertImg(file_dir)


def convertImg(path):
    f,e = os.path.splitext(path)
    convert_file = f+'.jpg'
    try:
        img = cv2.imread(path)
        cv2.imwrite(convert_file, img)
        print('convert %s sucessful!' % path)
    except:
        print('can not convert file %s' % path)


if __name__ == '__main__':
    checkConvert(convert_path)