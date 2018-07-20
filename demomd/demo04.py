#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

# -*- coding: utf-8 -*-


from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle
import time
import os

def rpt(img_path):
    story=[]
    stylesheet=getSampleStyleSheet()
    l = os.listdir(img_path)
    l.sort(key=lambda x: int(x[:-4]))
    filesize_now = 0
    filesize_limit = 1024
    imgpath = []
    for i in l:
        f = img_path + os.sep + str(i)
        file_size = int(os.path.getsize(f) / 1024)
        filesize_now += file_size
        if filesize_now >= filesize_limit:
            break
        imgpath.append(f)

    print(imgpath)
    component_data = []
    col_width = []
    for i in imgpath:
        #图片，用法详见reportlab-userguide.pdf中chapter 9.3 Image
        img = Image(i)
        img.drawHeight = 500
        img.drawWidth = 500

        #表格数据：用法详见reportlab-userguide.pdf中chapter 7 Table
        component_data.append([img])
        col_width.append(500)
    print(col_width)
    #创建表格对象，并设定各列宽度
    component_table = Table(component_data, colWidths=col_width)
    #添加表格样式
    component_table.setStyle(TableStyle([
    ('ALIGN',(-1,0),(-2,0),'RIGHT'),#对齐
    ('VALIGN',(-1,0),(-2,0),'MIDDLE'),  #对齐
    ]))
    story.append(component_table)

    doc = SimpleDocTemplate('bug.pdf')
    doc.build(story)

if __name__ == '__main__':
    rpt('C:/Users/Administrator/Pictures/ac1')