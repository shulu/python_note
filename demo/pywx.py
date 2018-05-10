#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from wxpy import *

bot = Bot(console_qr=True, cache_path=True)
friends_stat = bot.friends().stats()
a_friend = bot.friends()
#print(friends_stat)
# myself = bot.core.loginInfo['User']['NickName']
myself = bot.self.name
# print(friends_stat["province"].items())
# exit()

# 每一个元素是一个二元列表，分别存储地区和人数信息
friend_loc = []
for province, count in friends_stat["province"].items():

    if province == "":
        province = '未知区域'
    friend_loc.append([province, count])

# 对人数倒序排序
friend_loc.sort(key=lambda x: x[1], reverse=True)

print('%s 的好友地区统计' % myself)

#打印人数最多的十个地区
for item in friend_loc[:10]:
    print("%s 地区的好友有 %d个" % (item[0], item[1]))


# 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

# 发送消息给自己
# bot.self.send('Hello world')
# 给文件传输助手发送消息
# bot.file_helper.send('Hello World!')

# @bot.register()
# def print_message(msg):
#    print('[auto reply]'+msg.text)
#    return msg.text

# 进入Python命令行，让程序保持运行
# embed()