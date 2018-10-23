import requests
from lxml import etree

url_pc = 'http://www.ip138.com:8080/search.asp'
url_phone = 'http://m.ip138.com/mobile.asp'
mobile = '13570274240'

payload = {'mobile':mobile}
result = requests.get(url_phone, params=payload)
#print(result.text)
r = etree.HTML(result.text.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))
area = r.xpath('//span/text()')[2]
area = str(area).split(' ')
print(mobile+' '+area[0]+' '+area[1])
