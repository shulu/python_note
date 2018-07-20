
import requests
import json, re

test_url = 'http://www.baidu.com' #这只是一个用来测试的网址，可以修改为目标网站
ip = '125.212.254.125'
port = 3128
proxies = {
        'http': 'http://{}:{}'.format(ip, port),
        'https': 'http://{}:{}'.format(ip, port),
    }
response1 = requests.get(test_url, proxies=proxies, timeout=3)
if response1.status_code == 200:
    print('代理IP已保存！')
else:
    print('代理IP请求不成功！')


exit()
print('http://jishi.cctv.com/2016/09/12/VIDAV12WqaPzU09IZWj2WgsK160912.shtml'.split('/')[6][:-6])

exit()
# response = requests.get('http://jishi.cctv.com/doc/shujubao/A/index.json')
txt = open('jsonp.text', 'r', encoding='utf-8').read()
txt = txt.replace('index_data(', '').replace(')', '')
print(json.loads(txt)['data']['defList'])
# print(re.findall(r"\w+\((.*)\)", txt))
# print((response.text))
exit()
a = [1,2,3,4,5,6]
a.extend([1,2,3])
print(a)

dict_demo = {'a':1,'b':2}
print(dict_demo)
dict_demo = [{'user_name': '一只撸狗'}, {'user_name': '起小点是大腿'}, {'user_name': '远离颠倒梦想'}, {'user_name': '野食小哥'}, {'user_name': '抽风的飞机'}, {'user_name': '长歌是大腿'}, {'user_name': 'STN工作室'}, {'user_name': '随从MT'}, {'user_name': '奥雷卡尔克斯'}, {'user_name': 'SteamParty'}]
for users in dict_demo:
    print(users['user_name'])

