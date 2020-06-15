#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/28
import requests
path="D:\\you belong with me.mp3"
url="http://isure.stream.qqmusic.qq.com/C400000Z7Sn40A1qmt.m4a?guid=2255109952&vkey=25E90F2FB866A6B6BE3BC4DEF1C71B07A7D2A373DCDD5C10D845380112A1EBC18EFB5FA0137756126B76DE2A51A1D598702D86EA11AFB71C&uin=0&fromtag=66"
kv={"User-Agent": "Mozilla"}
r=requests.get(url,headers=kv)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)