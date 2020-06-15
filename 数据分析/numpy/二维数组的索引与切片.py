#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import numpy as np
a=np.array([[0,5],[5,10],[10,15]])
print(a)
print(a[0])
print(a[:,0])
print(a[0:2])
print(a[:,0:2])
print(a[[0,1],[0,1]])
a[:,0]=0
print(a)
print(a>0)
a[a>0]=1
print(a)
