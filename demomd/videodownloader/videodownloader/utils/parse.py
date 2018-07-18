#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import json

def parse(response):

    data = response.text.replace('index_data(', '').replace(')', '')
    def_list = json.loads(data)[ 'data' ][ 'defList' ]
    if not def_list:
        return []
    return [x['url'] for x in def_list], def_list


def detail_parse(response):

    pass