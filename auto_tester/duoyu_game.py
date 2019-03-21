#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import requests
import hashlib
import json, time, random, csv, os, datetime


class duoyugame():

    def __init__(self):

        self.sess = self.start_get_session()
        self.game_url = 'http://h5.543911.com/game.php?id='
        self.user_url = 'http://sdkapi.543911.com/api/h5/user.php'
        self.login_url = 'http://sdkapi.543911.com/h5/login_skip.php'
        self.uname = ''
        self.ori_pwd = ''
        self.pwd = ''
        self.game_id = 34
        self.sess_id = ''
        self.uid = ''
        self.real_url = ''

    def main_hand(self):
        # self.game_id = game_id
        self.reg()
        self.get_info()
        self.get_real_url()
        self.set_account_info()
        pass

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


if __name__ == '__main__':

    #game_id = input('请输入要生成的游戏ID:')
    game = duoyugame()
    #game.main_hand(game_id)
    game.main_hand()
