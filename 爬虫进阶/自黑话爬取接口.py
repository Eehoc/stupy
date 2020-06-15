#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/30
import requests
import re
import PyInstaller
kv = {"User-Agent": "Mozilla/5.0"}
url = "https://api.btstu.cn/yan/api.php?charset=utf-8&encode=js"
r = requests.get(url, headers=kv)
html = r.text
r = html.replace("function text()", "")
data = re.findall("'(.*?)'", html)
print(data)
