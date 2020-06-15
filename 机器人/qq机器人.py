#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/6
import requests
from flask import flas
data = {
    'user_id':919368650,
    'message':'我是一个可爱的小机器人喵~',
    'auto_escape':False
}

api_url = 'http://127.0.0.1:5700/send_private_msg'
#酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700

r = requests.post(api_url,data=data)
print(r.text)