#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from pyquery import PyQuery

def parse(response):

    '''
    #zimu_list_content_1 > table > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(1) > a
    :param url:
    :return:
    '''
    jpy = PyQuery(response.text)
    jpy('#zimu_list_content_1 > table > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(1) > a')