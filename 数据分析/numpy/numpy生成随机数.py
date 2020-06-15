#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import numpy as np
np.random.seed(10)
a=np.random.rand(10,5)
print(a)
# seed使得每次随机都一样
print(np.random.randint(0,10,(5,5)))