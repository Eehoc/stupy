#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/11
from time import *
def 装饰器函数(函数):
    def wrapper():
        begain_time = time()
        函数()
        end_time = time()
        print("耗时%0.3f" % (end_time - begain_time))
    return wrapper



