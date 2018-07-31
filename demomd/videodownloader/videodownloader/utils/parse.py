#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from pyquery import PyQuery
import json
from lxml import etree
import re

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
    xp = etree.HTML(response.text)
    if 'jishi' in request_url:
        # print('here was jishi {}'.format(request_url))
        json_url = 'http://tv.cntv.cn/api/video/getvideo/{}'
        script = xp.xpath('//script/text()')
        vset = re.findall(r'(VSET[\d]{12})', script[12])

        pass
    elif 'tv.cctv.com' in request_url:
        # print('hera was tv')
        image = xp.xpath('//*[@id="page_body"]/div[7]/div/div[1]/div/img/@src')[ 0 ]
        title = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/h3/text()')[ 0 ].encode('ISO-8859-1').decode('utf-8')
        type = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[1]/span')[ 0 ].tail.encode('ISO-8859-1').decode('utf-8')
        num = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[2]')[ 0 ].tail.encode('ISO-8859-1').decode('utf-8')
        director = xp.xpath('//*[@id="page_body"]/div[7]/div/div[2]/div/p[3]')[ 0 ].tail.encode('ISO-8859-1').decode('utf-8')
        description =  xp.xpath('//*[@id="shuoqi"]/span')[ 0 ].tail.encode('ISO-8859-1').decode('utf-8')
        items = xp.xpath('//*[@id="fpy_ind04"]/dd')
        for it in range(1, len(items)):
            piece__href = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[1]/@href'.format(it))[ 0 ]
            piece_title = xp.xpath('//*[@id="fpy_ind04"]/dd[{}]/div[1]/a[1]/@title'.format(it))[ 0 ].encode(
                'ISO-8859-1').decode('utf-8')
