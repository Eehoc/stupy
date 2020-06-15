#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/25
import pandas as pd
a = {"name": ["王灿" ,"王敏" ,"王钰涵"] ,"age": ["20" ,"23" ,"6"] ,}
t1 = pd.DataFrame(a)
print(t1)
b = [{"name": "王灿" ,"age": "20"} ,{"name": "王敏" ,"age": "23"} ,{"name": "王钰涵" ,"age": "6"}]
t2 = pd.DataFrame(b)
print(t2)
