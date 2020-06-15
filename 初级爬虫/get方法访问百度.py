#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/26
import requests
r=requests.get("https://www.baidu.com/")
print(r.encoding)
print(r.apparent_encoding)
r.encoding=r.apparent_encoding
print(r.text)