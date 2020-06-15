#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/5
import wxpy
# 创建实例
bot=wxpy.Bot()
friend=bot.friends().search("凯莱")[0]
friend.send("我是一个机器人")
