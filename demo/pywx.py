#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from wxpy import *
from pyecharts import Bar, Pie

bot = Bot(console_qr=True, cache_path=True)

# bot.file_helper.send("{apikey：98f466650507488b836a9eea937fc211,密钥： 7a18332b77f41b94,userid:261407}")

friends = bot.friends()
for chat in friends:
    nick_name = chat.nick_name
    chat.get_avatar('./wx_avatar/'+nick_name+'.jpg')

exit()
friends_stat = bot.friends().stats()
a_friend = bot.friends()
#print(friends_stat)
# myself = bot.core.loginInfo['User']['NickName']
myself = bot.self.name
#print(list(friends_stat["sex"].items()))
exit()

# 每一个元素是一个二元列表，分别存储地区和人数信息
friend_loc = []
for province, count in friends_stat["province"].items():

    if province == "":
        province = '未知区域'
    friend_loc.append([province, count])

friend_sex = []
for sex, count in friends_stat["sex"].items():

    if sex == 1:
        sex = '好汉'
    elif sex ==2 :
        sex = '女侠'
    else:
        sex = '外星人'
    friend_sex.append([sex, count])

# 对人数倒序排序
friend_loc.sort(key=lambda x: x[1], reverse=True)

print('%s 的好友地区统计' % myself)

#打印人数最多的十个地区
for item in friend_loc[:10]:
    print("%s 地区的好友有 %d个" % (item[0], item[1]))

# print(list(map(lambda x:x[0], friend_loc)))

# exit()

# bar = Bar("'%s 的好友地区统计'" % myself)
# bar.add("人数", list(map(lambda x:x[0], friend_loc)), list(map(lambda x:x[1], friend_loc)), is_stack=True, mark_line=["min", "max"], mark_point=["average"])
# bar.render('wxpy_location.html')


pie = Pie("'%s 的好友统计'" % myself, width=900)
pie.add('', list(map(lambda x:x[0], friend_loc)), list(map(lambda x:x[1], friend_loc)), center=[25,50], radius=[0, 50], is_label_show=True, legend_pos='left')
pie.add('', list(map(lambda x:x[0], friend_sex)), list(map(lambda x:x[1], friend_sex)), center=[75, 50], radius=[0, 50], is_label_show=True, legend_pos='right')
pie.render('wxpy_location_pie.html')
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