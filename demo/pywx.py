#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from wxpy import *

bot = Bot(console_qr=True, cache_path=True)
friends_stat = bot.friends().stats()
a_friend = bot.friends()
print(friends_stat)

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