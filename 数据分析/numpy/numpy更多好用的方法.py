#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import numpy as np
t=np.array([range(0, 5), range(5, 10)])
print(t)
# 最大值的位置
print(np.argmax(t, axis=0))
print(np.argmax(t, axis=1))
print(np.zeros((5, 3)))
# 对角线为1的数组
print(np.eye(5))