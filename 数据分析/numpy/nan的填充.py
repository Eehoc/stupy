#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import numpy as np


def me(t):
    for i in range(t.shape[1]):
        temp = t[:,i]
        nan_num = np.count_nonzero(temp != temp)
        if nan_num != 0:
            not_nan = temp[temp == temp].mean()
            temp[np.isnan(temp)] = not_nan
    return t


def main():
    t = np.arange(12).reshape(3, 4).astype("float")
    t[2,2:] = np.nan
    print(t)
    t = me(t)
    print(t)


if __name__ == '__main__':
    main()
