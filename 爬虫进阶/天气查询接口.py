#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/30
globals = {
    'true': 0,
    'false': 1
}
import requests
kv={"User-Agent":"Mozilla/5.0"}
url="http://liuxingw.com/api/tianqi/api.php?location=咸宁"
r=requests.get(url,headers=kv)
r.encoding="utf-8"
data=r.json()
d=data["data"][0]
for k,v in d.items():
    print(k,"-->",v)
