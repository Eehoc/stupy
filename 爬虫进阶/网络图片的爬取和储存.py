#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/27
import requests
path="D:\\派大星.gif"
url="http://image.uczzd.cn/3805104256745469257.jpg?id=0"
r=requests.get(url)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)
