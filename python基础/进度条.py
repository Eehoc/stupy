#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/10
import time

length = 1000
for i in range(1, length + 1):
    percent = i / length
    bar = '▉' * int(i // (length / 50))
    time.sleep(0.01)
    print('\r进度条：|{:<50}|{:>7.1%}'.format(bar, percent), end='')
print('\n')