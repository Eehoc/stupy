#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/27
import requests
kv={"User-Agent": "Mozilla/5.0"}
path="D:\\想见你.mp3"
url="http://ws.stream.qqmusic.qq.com/C400003XfCwi4ORhLh.m4a?guid=2255109952&vkey=55E659F0EFA73491F1C8FAC4134E941B2568EAC654AE41156F04B5CF772BEF7CD0F36E94788C1524AD7186892F95B724CA0D220DA67E3110&uin=0&fromtag=66"
r=requests.get(url,headers=kv)
with open(path,"wb") as f:
    f.write(r.content)
