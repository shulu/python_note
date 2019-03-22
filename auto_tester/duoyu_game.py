#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
from selenium import webdriver
import hashlib
import json, time, random, csv, os, datetime, re


class duoyugame():

    def __init__(self):

        self.sess = self.start_get_session()
        self.game_url = 'http://h5.543911.com/game.php?id='
        self.user_url = 'http://sdkapi.543911.com/api/h5/user.php'
        self.login_url = 'http://sdkapi.543911.com/h5/login_skip.php'
        self.pay_url = 'http://h5.543911.com/iframe/pay.php'
        self.yb_url = 'https://lcwslogpy.newyx.jiulingwan.com/duoyu/payment?'
        self.uname = ''
        self.ori_pwd = ''
        self.pwd = ''
        self.game_id = 34
        self.sess_id = ''
        self.uid = ''
        self.real_url = ''
        self.login_cookie = ''
        self.server_id = 0
        self.order_id = ''

    def main(self):
        # self.game_id = game_id
        self.reg()
        self.get_info()
        self.get_real_url()
        self.set_account_info()
        self.handler_game()
        pass

    def yb(self):
        pay_key = 'c315e07b11e8426c8371c6d00fc9b4fd'
        payload = {
            "uid": 24,
            "money": 39830,
            "time": str(int(time.time())),
            "sid": "66624406",
            "orderid": self.order_id,
            "ext": "39830|66624406",
            "flag": "1000元宝",
        }
        md5_str = payload['uid']+payload['money']+payload['time']+payload['sid']+payload['orderid']+payload['ext']+pay_key
        md5_str = self.get_token(md5_str)
        payload['flag'] = md5_str
        r = requests.get(self.yb_url, params=payload)
        print(r.text)
        pass

    def order(self):
        payload = {
            "game_id": 24,
            "server_id": 39830,
            "uid": 1,
            "role_id": "66624406",
            "role_name": "眼泪辉煌",
            "money": 10,
            "ext": "39830|66624406",
            "product_name": "1000元宝",
            "user_name": "sarcasme",
            "agent_id": 200000,
            "site_id": 200000,
            "tw_game_id": ""
        }
        r = self.sess.get(self.pay_url, params=payload)
        pay_info = json.loads(r.text)
        self.order_id = pay_info['data']['orderid']

    def reg(self):
        self.set_user_pwd()
        payload = {
            "do": "reg",
            "user_name": self.uname,
            "password": self.pwd,
            "re_password": self.pwd,
            "agent_id": 10003,
            "site_id": 10003,
            "cplaceid": 10003,
            "passType": 2,
            "game_id": self.game_id,
        }
        r = self.sess.get(self.user_url, params=payload)
        user_info = json.loads(r.text)
        self.uid = user_info['data']['login']['uid']

    def login(self):
        payload = {
            "do": "login",
            "user_name": self.uname,
            "password": self.pwd,
            "agent_id": 10003,
            "site_id": 10003,
            "cplaceid": 10003,
            "passType": 2,
            "game_id": self.game_id,
        }
        r = self.sess.get(self.user_url, params=payload)
        self.login_cookie = {
            'loginreg':r.cookies["loginreg"],
            'login_time':r.cookies["login_time"],
            'login_name':r.cookies["login_name"],
            'login_ip':r.cookies["login_ip"],
            'PHPSESSID':r.cookies["PHPSESSID"]
        }
        self.sess_id = r.cookies["PHPSESSID"]

    def get_info(self):
        payload = {
            "do": "getInfo",
            "game_id": self.game_id,
            "server_id": 1,
        }
        r = self.sess.get(self.user_url, params=payload)
        data = json.loads(r.text)
        self.sess_id = data['data']['sid']

    # 写入游戏对应信息
    def set_account_info(self):
        file_time = str(datetime.datetime.now().strftime('%Y-%m-%d'))
        file_name = './'+file_time+'.csv'
        state = os.path.exists(file_name)  # 判断路径是否存在
        if state:
            # 打开文件，追加a
            out = open(file_name, 'a', newline='')
            # 设定写入模式
            csv_write = csv.writer(out, dialect='excel')
            # 写入具体内容
            info = [self.uid, self.uname, self.ori_pwd, self.game_id, self.real_url]
            csv_write.writerow(info)
        else:
            # 打开文件，追加a
            out = open(file_name, 'w', newline='')
            # 设定写入模式
            csv_write = csv.writer(out, dialect='excel')
            # 写入头
            info = ['uid', 'username', 'password', 'game_id', 'game_url']
            csv_write.writerow(info)
            info = [self.uid, self.uname, self.ori_pwd, self.game_id, self.real_url]
            csv_write.writerow(info)

    # 获取真实游戏地址
    def get_real_url(self):
        payload = {
            "appid": self.game_id,
            "uid": self.uid,
            "uname": self.uname,
            "sessionid": self.sess_id,
            "logotype": 1
        }
        r = self.sess.get(self.login_url, params=payload, allow_redirects=False)
        self.real_url = r.headers['location']

    def start_get_session(self):
        session = requests.session()
        return session

    # 配置用户账号密码
    def set_user_pwd(self):
        """
        user
        $uname = 'yu'.substr(time(), -6);
        $uname = $uname.mt_rand(10, 99);
        pwd
        $chars = '123456789';
        $pwd   = '';
        for ($i = 0; $i < 6; $i++) {
            $pwd .= $chars[ mt_rand(0, strlen($chars) - 1) ];
        }
        """
        chars = '123456789'
        len_char = len(chars)
        t = 'yu'+str(int(time.time()))[:-6]
        self.uname = t+str(random.randint(10,99))
        pwd = ''
        for x in range(0,6):
            offset = random.randint(0, int(len_char)-1)
            pwd = pwd+chars[offset]
        self.ori_pwd = pwd
        self.pwd = self.get_token(pwd)
        #return {'uname':uname, 'pwd':pwd}

    def get_token(self,md5_str):
        # 生成一个md5对象
        m1 = hashlib.md5()
        # 使用md5对象里的update方法md5转换
        m1.update(md5_str.encode("utf-8"))
        token = m1.hexdigest()
        return token

    # 配置H5登录URL
    def set_gameurl(self, game_id):
        game_url = self.game_url + str(game_id)
        return game_url

    def handler_game(self):
        driver = webdriver.Chrome()
        driver.get(self.real_url)
        for key in self.login_cookie:
            driver.add_cookie({'name': key, 'value': self.login_cookie[key]})
        driver.get(self.real_url)
        server_ele = driver.find_element_by_class_name('selected-server').text
        self.server_id = re.sub("\D", "", server_ele)
        driver.find_element_by_xpath('//*[@id="curDf"]/p').click()
        #now_driver = driver.current_window_handle()
        print(driver.page_source)
        pass

if __name__ == '__main__':

    #game_id = input('请输入要生成的游戏ID:')
    game = duoyugame()
    #game.main_hand(game_id)
    game.main()
