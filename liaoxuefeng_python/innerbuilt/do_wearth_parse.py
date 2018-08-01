# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate
import json

data = {}
textlist = []
class WeatherSaxHandler(object):
    def start_element(self, name, attr):
        if not name in data:
            data[name] = []
        data[name].append({'attr' : attr})

    def char_data(self, text):
        textlist.append(text)

    def end_element(self, name):
        global textlist
        str = ''.join(textlist)
        data[name][-1]['text'] = str
        textlist = []


def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    location = data['yweather:location']
    forecast = data['yweather:forecast']
    return {
        'city': location[0]['attr']['city'],
        'country': location[0]['attr']['country'],
        'today': {
            'text': forecast[0]['attr']['text'],
            'low': forecast[0]['attr']['low'],
            'high': forecast[0]['attr']['high'],
        },
        'tomorrow': {
            'text': forecast[1]['attr']['text'],
            'low': forecast[1]['attr']['low'],
            'high': forecast[1]['attr']['high'],
        },
    }
    #可将数据写入json文件
    # with open('weather_data.json', 'w') as f:
    #     json.dump(data, f)

if __name__ == '__main__':
    from do_weather_xml import getWeatherXML
    xml = getWeatherXML()
    d = parse_weather(xml)
    print(str(d))

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

print(parse_weather(data))