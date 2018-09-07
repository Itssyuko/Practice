#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x,(int,float)): #如果是元组中的一个则返回true
        raise TypeError('bad oprand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
print(math.sin(10))