#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：王灿 time:2020/2/27
import requests
path="D:\\听风.mp3"
url="https://m701.music.126.net/20200227202547/b6e0894dc031f89ffe4e32e43f5d103b/jdyyaac/0759/550f/5153/033dc13759beac4fc7c7f9f4f7afd3a2.m4a"
r=requests.get(url)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)
