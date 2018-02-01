#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from urllib import request
import time
import zipfile
import os
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.pdfgen import canvas
import json

file_path = 'D:/products/'


# 获取网页信息
def getHtmlInfo(url):
    # url_path = url[24:]
    res = requests.get(url, timeout=10)
    is_ok = res.status_code
    if is_ok == 200:
        s = etree.HTML(res.text)
        return s

#获取描述和描述图片
def htmlDescription(s, pid):
    desc_content = s.xpath('//div[@class="list"][1]')
    desc_img = []
    allelem = desc_content[0].iter()
    for elem in allelem:
        if elem.tag == 'img':
            elem.getparent().remove(elem)
            desc_img.append('https:'+elem.attrib['data-original'])
           # print('https:'+elem.attrib['data-original'])
    img_path = getImg('desc_img', desc_img, pid)
    description = etree.tostring(desc_content[0], pretty_print=True, encoding='utf-8')
    filter_desc = description.decode().replace('\n', '').replace('\t', '')
    all_desc = '<html>'+filter_desc+'</html>'
    path = file_path+pid+'/pro'+pid+'.html'
    f = open(path,'w', encoding='utf-8')
    f.write(all_desc)
    f.close()
    # print(all_desc)
    return img_path

# 压缩图片
def zipBigImg(s, pid):
    links = s.xpath('//a[contains(@big,"http")]')
    big_img_list = []
    for index in range(len(links)):
        big_img_list.append(links[index].attrib['big'])
    path = getImg('main_img',big_img_list, pid)
    return path

#下载图片
def getImg(folder, imglist, pid):
    now_path = file_path + pid + '/'+folder+'/'
    checkdir(now_path)
    for i in range(len(imglist)):
        f = open(now_path+str(i+1)+'.jpg',"wb")    #打开文件
        req = request.urlopen(imglist[i], timeout=10)
        buf = req.read()              #读出文件
        f.write(buf)                  #写入文件
        f.close()
        print("now writing "+ folder + '/' + str(i+1) + '.jpg')
        time.sleep(1)
    return now_path

#压缩文件
def writeZip(path, pid, file_name):
    azip = zipfile.ZipFile(file_path + pid + '/' + file_name, mode='w', compression=zipfile.ZIP_DEFLATED)
    for current_path, subfolders, filesname in os.walk(path):
        #print(current_path, subfolders, filesname)
        #  filesname是一个列表，我们需要里面的每个文件名和当前路径组合
        for file in filesname:
            # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
            azip.write(os.path.join(current_path, file), file)
        # 关闭资源
        azip.close()

#生成图片PDF
def convert_images_to_pdf(img_path, pid, pdf_name):
    pages = 0
    (w, h) = portrait(A4)
    c = canvas.Canvas(file_path + pid + '/' + pdf_name, pagesize = portrait(A4))
    l = os.listdir(img_path)
    l.sort(key= lambda x:int(x[:-4]))
    filesize_now = 0
    filesize_limit = 1024
    for i in l:
        f = img_path + os.sep + str(i)
        file_size = int(os.path.getsize(f)/1024)
        filesize_now += file_size
        if filesize_now >= filesize_limit:
            break
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()


def checkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


if __name__ == '__main__':
    with open("info.json", 'r') as prod_info:
        load_info = json.load(prod_info)
        for p in load_info['RECORDS']:
            pid = str(p['pid'])
            s = getHtmlInfo(p['url'])
            desc_path = htmlDescription(s, pid)
            convert_images_to_pdf('D:/products/'+pid+'/desc_img/', pid, 'pro'+pid+'.pdf')
            now_path = zipBigImg(s, pid)
            # zip_name = 'pro1227745.zip'
            writeZip(now_path, pid , 'pro'+pid+'zip')

    # s = getHtmlInfo('https://www.banggood.com/-p-1227745.html')
    # desc_path = htmlDescription(s, '1227745')
    # convert_images_to_pdf('D:/products/1227745/desc_img/', '1227745', 'pro1227745.pdf')
    # now_path = zipBigImg(s, '1227745')
    # zip_name = 'pro1227745.zip'
    # writeZip(now_path, '1227745', zip_name)