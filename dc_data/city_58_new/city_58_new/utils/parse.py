#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from pyquery import PyQuery


def parse(response):
    """
    抓取小区列表页面： http://cd.58.com/xiaoqu/11487/
    返回列表页所有的小区url
    :param:response
    :return
    """
    jpy = PyQuery(response.text)

    tr_list = jpy('#infolist > div.listwrap > table > tbody > tr').items()

    result = set()  #result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr(' td.info > ul > li.tli1 > a').attr('href')  #爬取各个小区的url
        result.add(url)

    return result


def xiaoqu_parse(response):
    """
    小区详情页匹配代码样例url:http://cd.58.com/xiaoqu/shenxianshudayuan/
    返回这个小区的详细信息的dict字典，主要信息包括小区名称，小区参考房价，小区地址，小区建筑年代
    :param:response
    :return:
    """

    result = dict()
    jpy = PyQuery(response.text)
    result['name'] = jpy('body > div.bodyItem.bheader > div > h1 > span').text()
    result['reference_price'] = jpy('body > div.bodyItem.bheader > div > dl > dd:nth-child(1) > span.moneyColor').text()
    result['address'] = jpy('body > div.bodyItem.bheader > div > dl > dd:nth-child(3) > span.ddinfo')\
        .text().replace('查看地图', '')   #得到地址详情，去除“查看地图”，如 “ 紫荆西路6号 查看地图”，将“查看地图”替换为“”
    result['times'] = jpy('body > div.bodyItem.bheader > div > dl > dd:nth-child(5)').text().split()
    result['times'] = result['times'][2]  #取出建筑年代
    return result


def get_ershou_price_list(response):
    """
    页面链接样例:http://cd.58.com/xiaoqu/shenxianshudayuan/ershoufang/
    匹配二手房列表页面的所有房价信息
    返回一个价格的列表list
    :param:response
    :return:
    """

    jpy = PyQuery(response.text)
    price_tag = jpy('td.tc > span:nth-child(3)').text().split()
    price_tag = [i[:-3] for i in price_tag]   #遍历price_tag截取到倒数第三个元素
    return price_tag


def chuzu_list_pag_get_detail_url(response):
    """
    页面链接样例:http://cd.58.com/xiaoqu/shenxianshudayuan/chuzu/
    获取出租列表页所有详情页url
    返回一个url的列表list
    :param:response
    :return:
    """
    jpy = PyQuery(response.text)
    a_list = jpy('tr > td.t > a.t').items()
    url_list = [a.attr('href') for a in a_list]  #遍历a_list
    return url_list


def get_chuzu_house_info(response):
    """
    获取出租详情页的相关信息
    返回一个dict包含：出租页标题，出租价格，房屋面积，房屋类型（几室几厅）
    :param:response
    :return:
    """
    jpy = PyQuery(response.text)
    result = dict()
    result['name'] = jpy('body > div.main-wrap > div.house-title > h1').text()
    result['zu_price'] = jpy('body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > '
                          'div.house-basic-desc > div.house-desc-item.fl.c_333 > div > span.c_ff552e > b').text()

    result['type'] = jpy('body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-basic-desc'
                         ' > div.house-desc-item.fl.c_333 > ul > li:nth-child(2) > span:nth-child(2)').text()

    result['type'], result['mianji'], *_ = result['type'].split()
    return result


if __name__ == '__main__':
    import requests
    r = requests.get('http://cd.58.com/zufang/31995551807162x.shtml')
    get_chuzu_house_info(r)