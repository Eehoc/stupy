#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/27
import requests
path="D:\\Nasa.mp3"
url="https://m10.music.126.net/20200227202937/71802c459d2c2c3963386d6459d15ebc/yyaac/055d/010c/0f5d/2770661d9d6f2ee1963b87d08ab94d55.m4a"
r=requests.get(url)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)
