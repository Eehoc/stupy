#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/28
import requests
url="http://ws.stream.qqmusic.qq.com/C400000ck2pC1vlCqe.m4a?guid=2255109952&vkey=79B2145272800E778406696FC1A4A0BF5CCFF101A2B6211A3707A2C398884C5D6AC771F0BBE39F869A1200EE2A5982FBA800C351C2D021C0&uin=0&fromtag=66"
path="D:\\love story me.mp3"
kv={"User-Agent": "Mozilla"}
r=requests.get(url,headers=kv)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)