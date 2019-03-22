#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
token_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mP7ZaUhPIU6Zv8ogQEmklAho&client_secret=3GcaPpbDtSTs1wcXb814DBNiB5C07lPD'
api_host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
r = requests.get(token_host, headers={'Content-Type': 'application/json; charset=UTF-8'})
content = r.text
if (content):
    print(content)