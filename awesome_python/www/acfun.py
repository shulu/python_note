# -*- coding: utf-8 -*-

import io
import sys
import requests
import json
import pymysql
from models import next_id

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

# r.status_code #响应状态码
# r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#*特殊方法*#
# r.json() #Requests中内置的JSON解码器
# r.raise_for_status() #失败请求(非200响应)抛出异常


def store(data):
    # 打开数据库连接
    con = pymysql.connect(
        #user="www-data",
        #password="www-data",  #连接数据库，不会的可以看我之前写的连接数据库的文章
        user="root",
        password="123",
        port=3306,
        # host="127.0.0.1",
        host="192.168.217.131",
        db="awesome",
        charset="utf8"
    )
    # 使用cursor()方法获取操作游标
    cur = con.cursor()
    sql = "INSERT INTO `acfun_focus` (id, user_name, user_id ,user_img,avatar,sign,title,title_img,url,release_date,description ,tags ,video_time) VALUES ('%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d')" % data
    cur.execute(sql)
    con.commit()


def get_data():
    s = requests.session()
    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Content-Length':'37',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'www.acfun.cn',
        'Origin':'http://www.acfun.cn',
        'Referer':'http://www.acfun.cn/login/?returnUrl=http://www.acfun.cn/member/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    login_data = {'username':'13570274240','password':'SHU1202LU'}
    s.post('http://www.acfun.cn/login.aspx',data=login_data,headers=headers)
    url = 'http://www.acfun.cn/member/publishContent.aspx?isGroup=0&groupId=-1&pageSize=10&pageNo='
    _range = ['1','2','3','4', '5', '6', '7']
    for x in _range:
        real_url = url+x
        # 获取请求信息
        data = s.get(real_url)
        # 将json字符串转成dict
        decode_data = json.loads(data.text)
        # {'pageNo': 1, 'pageSize': 10, 'totalCount': 2801, 'totalPage': 281, 'prePage': 1, 'nextPage': 2}
        # page = decode_data['page']
        contents = decode_data['contents']
        # print(contents[0])
        for item in contents:
            focus_id = next_id()
            # acfun时间多000
            release_date = str(item['releaseDate'])[:-3]

            # Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代:
            if item.__contains__('sign'):
                sign = item['sign']
            else:
                sign = ''
            data = (
                focus_id,
                item['username'], item['userId'], item['userImg'],
                item['avatar'], sign, item['title'],
                item['titleImg'], 'http://www.acfun.cn'+item['url'], release_date,
                item['description'], item['tags'], item['time']
            )
            store(data)


if __name__ == '__main__':
    get_data()
    print('get data successful!')



