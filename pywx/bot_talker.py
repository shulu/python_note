#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')

# 指定一个好友
lizelin = bot.friends().search('李泽霖')[0]

# 查看他的 puid
print(lizelin.puid)
# 'edfe8468'

lizelin.send('测试下自动回复啊 沙雕')

xiaoi = XiaoI('open_J5eWt4nfyyST', 'iW87PcbrL718wKrvItfU')

# 使用小 i 机器人自动与指定好友聊天
@bot.register(lizelin)
def reply_my_friend(msg):
    xiaoi.do_reply(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register(lizelin)
# def reply_my_friend(msg):
#    return 'received: {} ({})'.format(msg.text, msg.type)


# 进入 Python 命令行、让程序保持运行
embed()