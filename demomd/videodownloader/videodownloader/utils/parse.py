#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from pyquery import PyQuery
import json

def parse(response):

    data = response.text.replace('index_data(', '').replace(')', '')
    def_list = json.loads(data)[ 'data' ][ 'defList' ]
    if not def_list:
        return []
    return [x['url'] for x in def_list], def_list


def detail_parse(response):

    """
    #page_body > div:nth-child(9) > div > div.right > div > h3 title
    #page_body > div:nth-child(9) > div > div.right > div > p:nth-child(3) type
    #page_body > div:nth-child(9) > div > div.right > div > p:nth-child(5) director
    #zhankai description
    #fpy_ind03 single description
    #chbox01 > div.mtab_con > div:nth-child(3) > div > div.list_box video list
    :param response:
    :return:
    """
    jpy = PyQuery(response.text)