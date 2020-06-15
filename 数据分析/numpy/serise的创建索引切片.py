#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import pandas as pd
t = pd.Series([1,2,3,4,5,6,])
print(t)
t1=pd.Series([1,2,3,4,5,6,],index=list("abcdef"))
print(t1)
print(t1["a"])
print(t1[["a","b","c"]])
print(t1[0])
print(t1[[0,2,5]])
print(t1[:2])