#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from PIL import Image, ImageSequence, ImageOps, ImageEnhance
import pytesseract

# 读取GIF
im = Image.open("origin.gif")

# GIF图片流的迭代器
items = ImageSequence.Iterator(im)

index = 0
# 遍历图片流的每一帧
for frame in items:
    print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
    frame.save("./pieces/av_girl_%d.png" % index)
    index += 1

# frame0 = items[0]
# frame0.save("./pieces/image.png")
# 上面都是导包，只需要下面这一行就能实现图片文字识别
# text=pytesseract.image_to_string(Image.open('new_name.png'))
# print(text)
#读入图片
# image = Image.open('./pieces/image.png')
# image = image.convert('L')
# image = ImageOps.invert(image)
# image = image.convert('1')
#反转
# inverted_image = ImageOps.invert(image)
#保存图片
# image.save('new_name.png')