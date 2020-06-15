#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/23
import numpy as np
# 使用numpy创建数组，ndarray类型
t=np.array([0,1,2])
print(t)
print(type(t))
print("*"*20)
t1=np.array(range(0,3),dtype="float")
print(t1)
print("*"*20)
t2=np.arange(0,3,dtype="int64")
print(t2)
print(t2.dtype)
print("*"*20)
a=np.array(range(0,6),dtype="bool")
# 存放数据的类型,在创建数组的时候可以指定。
print(t.dtype)
print(t1.dtype)
print(t2.dtype)
print(a)
# 调整数据类型
a=a.astype("int8")
print(a)
print(t.dtype)
c=np.array([[1,2,3],[4,5,6]])
print(c.shape)
c=c.reshape(3,2)
print(c)