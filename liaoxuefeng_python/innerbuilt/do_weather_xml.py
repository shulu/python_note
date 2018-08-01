# -*- coding: utf-8 -*-

from urllib import request, parse

def getWeatherXML():
    baseurl = 'https://query.yahooapis.com/v1/public/yql?'
    yql_query = 'select * from weather.forecast where woeid=2151330 And u="c"'
    yql_url = baseurl + parse.urlencode({'q':yql_query, 'format': 'xml'})
    with request.urlopen(yql_url) as page:
        str = page.read().decode('utf-8')
        return str

if __name__ == '__main__':
    str = getWeatherXML()
    with open('weather.xml', 'w') as f:
        f.write(str)