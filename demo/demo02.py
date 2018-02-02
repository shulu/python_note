#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import RequestException
from lxml import etree
from urllib import request
import time
import zipfile
import os
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle
import json

file_path = 'D:/products/'

# 获取网页信息
def getHtmlInfo(info):
    # url_path = url[24:]
    try:
        header = {
            'referer':'https://www.banggood.com',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        res = requests.get(info['url'], headers=header, timeout=10)
        is_ok = res.status_code
        if is_ok == 200:
            s = etree.HTML(res.text)
            return s
    except RequestException as e:
        info['fail_reason'] = '错误原因:'+str(e)
        content = json.dumps(info)
        open('fail_product.json', 'a').write(content+',\n')
        #print('出现错误， 错误原因: ', e)


#获取描述和描述图片
def htmlDescription(s, pid):
    desc_content = s.xpath('//div[@class="list"][1]')
    desc_img = []
    allelem = desc_content[0].iter()
    for elem in allelem:
        if elem.tag == 'img':
            elem.getparent().remove(elem)
            attr_dict = elem.attrib
            if attr_dict.has_key('data-original'):
                is_http = elem.attrib['data-original']
                if is_http.startswith( 'http' ):
                    continue
                desc_img.append('https:'+elem.attrib['data-original'])
            # print('https:'+elem.attrib['data-original'])
    img_path = getImg('desc_img', desc_img, pid)
    description = etree.tostring(desc_content[0], pretty_print=True, encoding='utf-8')
    #print(description)
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
    if imglist:
        for i in range(len(imglist)):
            jpg_path = now_path+str(i+1)+'.jpg'
            if os.path.exists(jpg_path):
                continue
            header = {
                'referer': 'https://www.banggood.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            }
            try:
                ir = requests.get(imglist[i], headers=header, timeout=15)
                if ir.status_code == 200:
                    open(jpg_path, 'wb').write(ir.content)
                print("now writing " + folder + '/' + str(i + 1) + '.jpg')
                time.sleep(1)
            except RequestException as e:
                fail_img = json.dumps({'url':imglist[i], 'folder':jpg_path, 'fail_reason':'错误原因:'+str(e)})
                open('img_fail.json', 'a').write(fail_img+',\n')
                #print('出现错误， 错误原因: ', e)
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


# 判断图片是否完整
def is_valid_jpg(jpg_file):
    """判断JPG文件下载是否完整 """
    if jpg_file.split('.')[-1].lower() == 'jpg':
        with open(jpg_file, 'rb') as f:
            f.seek(-2, 2)
            return f.read() == '\xff\xd9'
    else:
        return True

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


def rpt(img_path, pid, pdf_name):
    story=[]
    l = os.listdir(img_path)
    if l :
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
        #创建表格对象，并设定各列宽度
        component_table = Table(component_data, colWidths=col_width)
        #添加表格样式
        component_table.setStyle(TableStyle([
        ('ALIGN',(-1,0),(-2,0),'RIGHT'),#对齐
        ('VALIGN',(-1,0),(-2,0),'MIDDLE'),  #对齐
        ]))
        story.append(component_table)

        doc = SimpleDocTemplate(file_path + pid + '/' + pdf_name)
        doc.build(story)



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
            s = getHtmlInfo(p)
            if s != None:
                desc_path = htmlDescription(s, pid)
                rpt(desc_path, pid, 'pro'+pid+'.pdf')
                main_path = zipBigImg(s, pid)
                writeZip(main_path, pid , 'pro'+pid+'.zip')
    #s = getHtmlInfo('https://www.banggood.com/Wholesale-3Port-1_3B-HDMI-Splitter-Switch-Switcher-For-HDTV-1080P-p-28012.html')
    #desc_content = s.xpath('//div[@class="list"][1]')
    #desc_content = etree.tostring(desc_content[0], pretty_print=True, encoding='utf-8')
    # convert_images_to_pdf('D:/products/1227745/desc_img/', '1227745', 'pro1227745.pdf')
    # now_path = zipBigImg(s, '1227745')
    # zip_name = 'pro1227745.zip'
    # writeZip(now_path, '1227745', zip_name)