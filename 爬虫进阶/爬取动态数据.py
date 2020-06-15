#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/22
import time
import requests
import re
kv={"User-Agent":"Mozilla/5.0"}
for page in range(1,20):
    url="https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_dual_class=&keyword=&page="+str(page)+"&province_id=11&request_type=1&school_type=&signsafe=&size=20&sort=view_total&type=&uri=apigkcx/api/school/hotlists"
    r=requests.get(url,headers=kv)
    data=r.json()
    list=data["data"]["item"]
    for i in range(len(list)):
        print("{}".format(list[i]["name"]))