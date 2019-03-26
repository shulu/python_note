#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')

# 指定xiaodan
xiaodan = bot.friends().search('王晓丹')[0] #e7907b07
#lizelin = bot.friends().search('李泽霖')[0] #2672d0d1

# 指定小冰
xiaobing = bot.mps().search('小冰')[0] #fcbc04ef

# 查看他的 puid
# print(xiaodan.puid)
# print(lizelin.puid)
# print(xiaobing.puid)

xiaodan.send('hi 我们开始聊天咯')

@bot.register([xiaodan, xiaobing])
def auto_reply(msg):
    sender_id = msg.sender.puid
    if sender_id == 'e7907b07':
        xiaobing.send(msg.text)
        # msg.forward(xiaobing)
    elif sender_id == 'fcbc04ef':
        xiaodan.send(msg.text)
        # msg.forword(xiaodan)

embed()