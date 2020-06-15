#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import numpy as np
a=np.arange(0,10)
b=np.arange(10,20)
print(a)
print(b)
# 竖直拼接
v=np.vstack((a,b))
# 水平拼接
h=np.hstack((a,b))
print(v)
print(h)