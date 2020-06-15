#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/28
import requests
path="D:\\Blank space.mp3"
url="http://110.52.197.23/amobile.music.tc.qq.com/C400004Ks0Ff0eQ4JR.m4a?guid=2255109952&vkey=A64DC56E435C0A4EEB943E2958C8BC4FA9EC82651C184D051381E6FE3FC2A9C95B8631C87F972CCC2E37A1067A2F2D66128F2169DB7C949E&uin=0&fromtag=66"
r=requests.get(url)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)