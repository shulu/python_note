#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
__author__ = 'SarcasMe'
import os, math
from wxpy import *
from pyecharts import Bar, Pie
from pyecharts import configure
import re
import jieba
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

class GenerateWxInfo():

    def __init__(self):

        # myself = bot.core.loginInfo['User']['NickName']
        self.login_wx()
        self.avatar_filename = './wx_avatar/' + self.login_user + '/avatar.png'
        my_friend = self.bot.friends().search(u'老婆')[ 0 ]
        my_friend.send_image(self.avatar_filename)
        # self.avatar_path = './wx_avatar/'+self.login_user+'/avatar/'
        # self.avatar_filename = './wx_avatar/'+self.login_user+'/avatar.png'
        # self.wd_path = './wx_wordclouds/'
        # self.wd_txt_path = self.wd_path+self.login_user+'_wx_singnature.txt'
        # self.wd_filename = self.wd_path+self.login_user+'.jpg'
        # self.las_path = './wx_locationandsex/'
        # self.las_filename = self.las_path+self.login_user+'_locationandsex.png'
        # self.drawLocationAndSex()
        # self.getFriendsAvatarAndSignature()
        # self.concat_img()
        # self.generate_wordclouds()
        # self.send_to_self()

    def login_wx(self):

        self.bot = Bot(console_qr=True, cache_path=True)
        self.login_user = self.bot.self.name
        self.friends = self.bot.friends()
        self.friends_stat = self.bot.friends().stats()

    def getFriendsLocation(self):

        # 每一个元素是一个二元列表，分别存储地区和人数信息
        friend_loc = []
        for province, count in self.friends_stat[ "province" ].items():

            if province == "":
                province = '未知区域'
            friend_loc.append([ province, count ])
            # 对人数倒序排序
            friend_loc.sort(key=lambda x: x[ 1 ], reverse=True)

            # print('%s 的好友地区统计' % self.login_user)
            # 打印人数最多的十个地区
            # for item in friend_loc[ :10 ]:
            #    print("%s 地区的好友有 %d个" % (item[ 0 ], item[ 1 ]))
        return friend_loc

    def getFriendsSex(self):

        friend_sex = [ ]
        for sex, count in self.friends_stat[ "sex" ].items():

            if sex == 1:
                sex = '好汉'
            elif sex == 2:
                sex = '女侠'
            else:
                sex = '外星人'
            friend_sex.append([ sex, count ])
        return friend_sex

    def getFriendsAvatarAndSignature(self):

        signature_list = [ ]
        for chat in self.friends:
            nick_name = chat.nick_name
            signature = chat.signature
            if signature != "":
                # 过滤换行空格
                signature = signature.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
                # 过滤html代码
                signature = re.sub(r'</?\w+[^>]*>', '', signature)
                # 过滤特殊字符
                signature = re.sub(r"[\s+.!/_,$%^*(+"')]+|[+——()?【】“”！，。？、~@#￥%……&*（）丶·๑•̀ㅂ́و✧ ～:3」∠❀]+', "", signature)
                signature_list.append(signature)
            if os.path.exists(self.avatar_path):
                file = self.avatar_path + nick_name + '.jpg'
                if os.path.exists(file):
                    pass
                    # print('%s file is exists' % file)
                else:
                    chat.get_avatar(save_path=file)
            else:
                os.makedirs(self.avatar_path)
                chat.get_avatar(save_path=self.avatar_path+nick_name+'.jpg')

        if os.path.exists(self.wd_txt_path):
            pass
            # print('%s file is exists' % self.wd_path+self.login_user+'_wx_singnature.txt')
        else:
            text = " ".join(signature_list)
            with open(self.wd_txt_path, 'a', encoding='utf-8') as f:

                wordlist = jieba.cut(text, cut_all=True)
                word_space_split = " ".join(wordlist)
                f.write(word_space_split + '\n')
                f.close()

    def drawLocationAndSex(self):

        # 将这行代码置于首部
        if os.path.exists(self.las_filename):
            print('%s file is exists' % self.las_filename)
        else:
            friend_loc = self.getFriendsLocation()
            friend_sex = self.getFriendsSex()
            pie = Pie("好友统计", width=900)
            pie.use_theme('macarons')
            pie.add('', list(map(lambda x: x[ 0 ], friend_loc)), list(map(lambda x: x[ 1 ], friend_loc)),
                    center=[ 25, 50 ], radius=[ 0, 50 ], is_label_show=True, legend_pos='left')
            pie.add('', list(map(lambda x: x[ 0 ], friend_sex)), list(map(lambda x: x[ 1 ], friend_sex)),
                    center=[ 75, 50 ], radius=[ 0, 50 ], is_label_show=True, legend_pos='right')
            # pie.render('wxpy_location_sex_pie.html')
            pie.render(path=self.las_filename)
            # 修改输出扩展名为.jpeg
            # img = Image.open(self.las_filename)
            # rgb_img = img.convert('RGB')
            # rgb_img.save(self.las_path+self.login_user+'_locationandsex.jpg')

    def concat_img(self):

        if os.path.exists(self.avatar_filename):
            # print('%s file is exists' % self.avatar_filename)
            pass
        else:
            # 获取所有图片
            ls = os.listdir(self.avatar_path)
            # print(ls)

            # sqrt返回平方根
            # print(int(math.sqrt(float(640*640)/48)))
            each_size = int(math.sqrt(float(640 * 640) / len(ls)))
            lines = int(640 / each_size)
            image = Image.new('RGB', (640, 640))
            x = 0
            y = 0
            for i in range(0, len(ls)):

                try:
                    img = Image.open(self.avatar_path + ls[ i ])
                except IOError:
                    print('Error')
                else:
                    img = img.resize((each_size, each_size), Image.ANTIALIAS)
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == lines:
                        x = 0
                        y += 1
            image.save(self.avatar_filename)

    def generate_wordclouds(self):

        text = open(self.wd_txt_path, encoding='utf-8').read()
        coloring = np.array(Image.open("./alice.png"))
        wc = WordCloud(
            background_color="white",
            max_words=2000,
            mask=coloring,
            max_font_size=40,
            random_state=42,
            font_path=r"C:\simhei.ttf"
        )
        # generate word cloud
        wc.generate(text)
        # create coloring from image
        image_colors = ImageColorGenerator(coloring)
        wc.to_file(self.wd_filename)

    def send_to_self(self):

        # self.bot.file_helper.send("{apikey：98f466650507488b836a9eea937fc211,密钥： 7a18332b77f41b94,userid:261407}")
        # 发送文本
        # my_friend.send('Hello, WeChat!')
        # 发送图片
        self.bot.file_helper.send_image(self.avatar_filename)
        self.bot.file_helper.send_image(self.wd_filename)
        self.bot.file_helper.send_image(self.las_filename)
        # 发送视频
        # my_friend.send_video('my_video.mov')
        # 发送文件
        # my_friend.send_file('my_file.zip')
        # 以动态的方式发送图片
        # my_friend.send('@img@my_picture.png')


if __name__ == '__main__':

    GenerateWxInfo()