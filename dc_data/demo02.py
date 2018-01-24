# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = "https://book.douban.com/subject/26708119/comments/"
r = requests.get(url).text

#print(r)

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')
#print(s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()'))
#print(s.xpath('//div[@class="comment"]/p/text()'))

#with open('pinlun.txt', 'w', encoding='utf-8') as f:
#    for i in file:
#        f.write(i)

import pandas as pd

df = pd.DataFrame(file)
#print(df)
#df.to_csv('pinglun.csv')
df.to_excel('pinglun.xlsx')


