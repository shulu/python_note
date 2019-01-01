#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from pyquery import PyQuery
import json
from lxml import etree
import re
import requests

def parse(response):

    data = response.text.replace('index_data(', '').replace(')', '')
    def_list = json.loads(data)[ 'data' ][ 'defList' ]
    if not def_list:
        return []
    return [x['url'] for x in def_list], def_list


def detail_parse(response):

    """
    # tv.cctv.com
    //*[@id="page_body"]/div[7]/div/div[1]/div/img -image
    //*[@id="page_body"]/div[7]/div/div[2]/div/p[1] -title
    //*[@id="page_body"]/div[7]/div/div[2]/div/p[2] -type
    //*[@id="page_body"]/div[7]/div/div[2]/div/p[3] -director
    //*[@id="zhankai"] -description
    //*[@id="fpy_ind04"]/dd[2] -video list
    # jishi.cctv.com
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/div/img -image
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td[2]/a -title
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[2]/td[2]/a -type
    //*[@id="page_body"]/div[4]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[4]/td[2] -director
    //*[@id="foldtext"]/text() -description
    //*[@id="ypdianbo"]/div/ul/li/div[1]/a[1] -url
    :param response:
    :return:
    """
    # jpy = PyQuery(response.text)
    request_url = response.url
    encoding = response.encoding
    xp = etree.HTML(response.text)
    if 'jishi' in request_url:
        # print('here was jishi {}'.format(request_url))
        json_url = 'http://tv.cntv.cn/api/video/getvideo/{}'
        script = xp.xpath('//script/text()')
        vset = re.findall(r'(VSET[\d]{12})', script[12])[0]
        dl_url = 'http://tv.cntv.cn/api/video/getvideo/vsid_{}'.format(vset)
        dl_rq = requests.get(dl_url)
        video_info = json.loads(dl_rq.text)
        vsid = video_info[ 'videoset' ][ '0' ][ 'vsid' ]
        image = video_info[ 'videoset' ][ '0' ][ 'img' ]
        director = video_info[ 'videoset' ][ '0' ][ 'dy' ]
        num = video_info[ 'videoset' ][ 'count' ]
        video_url = video_info[ 'videoset' ][ '0' ][ 'url' ]
        video_name = video_info[ 'videoset' ][ '0' ][ 'name' ]
        video_date = video_info[ 'videoset' ][ '0' ][ 'nf' ]
        video_type = video_info[ 'videoset' ][ '0' ][ 'fl' ]
        video_desc = video_info[ 'videoset' ][ '0' ][ 'desc' ]
        # print(video_name + ' : ' + video_url)
        # print(video_info)
        video = video_info[ 'video' ]
        return {
            'info': {
                'vsid': vsid,
                'image':image,
                'director':director,
                'num': num,
                'video_url': video_url,
                'video_name': video_name,
                'video_date': video_date,
                'video_type': video_type,
                'video_desc': video_desc
            },
            'video': video
        }

    elif 'tv.cctv.com' in request_url:
        # print('hera was tv')
        video = []
        vsid = re.findall(r'(VID[\w]*)', request_url)[0]
        image = xp.xpath('//*[@id="page_body"]/div[7]/div/div[1]/div/img/@src')[ 0 ]
        video_name = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/h3/text()')[ 0 ].encode(encoding).decode('utf-8')
        video_type = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[1]/span')[ 0 ].tail.encode(encoding).decode('utf-8').strip()
        num = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[2]')[ 0 ].tail.encode(encoding).decode('utf-8').strip()
        director = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[3]')[ 0 ].tail.encode(encoding).decode('utf-8')
        video_desc =  xp.xpath('//*[@id="shuoqi"]/span')[ 0 ].tail.encode(encoding).decode('utf-8')
        publish_date = xp.xpath('/html/head/script/text()')[3]
        video_date = re.findall(r'([\d]{14})', publish_date)[0]
        items = xp.xpath('//*[@id="fpy_ind04"]/dd')
        for it in range(1, len(items)):
            piece_href = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[1]/@href'.format(it))[ 0 ]
            piece_img = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[2]/img/@src'.format(it))[ 0 ]
            piece_title = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[1]/@title'.format(it))[ 0 ].encode(encoding).decode('utf-8')
            vid = re.findall(r'(VID[\w]*)', piece_href)[0]
            video.append({
                'vsid':vsid,
                'order':it,
                'vid':vid,
                't':piece_title,
                'url':piece_href,
                'img':piece_img
            })
        return {
            'info': {
                'vsid': vsid,
                'image': image,
                'director': director,
                'num': num,
                'video_url': request_url,
                'video_name': video_name,
                'video_date': video_date,
                'video_type': video_type,
                'video_desc': video_desc
            },
            'video': video
        }
