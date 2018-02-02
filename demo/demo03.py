#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import os
# import urllib2
import time
from reportlab import platypus
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, landscape
from PIL import Image


image_file = "42.jpg"

im = Image.open(image_file)
im_width = im.size[0]
im_height = im.size[1]
size = int(im_width*5), int(im_height*5)
# 分割文件路径和后缀名
FilePath,Fileext = os.path.splitext(image_file)
# 设置保存后的文件格式
outImageFile = "{0}.jpg".format(FilePath)
# 打开并保存
im.thumbnail(size)
im.save(outImageFile)
# (w, h) = portrait(A4)
# # Use Canvas to generate pdf
# c = canvas.Canvas('reportlab_canvas.pdf', pagesize = portrait(A4))
#
# #c.setFillColorRGB(0,0.77,0.77)
# # say hello (note after rotate the y coord needs to be negative!)
# #c.drawString( 3*inch, 3*inch, "Hello World")
# c.drawImage(image_file, -0, 200, int(im_width/5), int(im_height/5))
# c.showPage()
# c.save()