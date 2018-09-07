#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
    # if not isinstance(a,b,c,(int)):
    #     raise TypeError('bad oprator type')

    delt = pow(b,2)-4*a*c

    if delt > 0:
        x1 = (-b+math.sqrt(delt))/(2*a)
        x2 = (-b-math.sqrt(delt))/(2*a)
        print('此方程有两个解：%s,%s' % (x1,x2))
        return x1,x2
    elif delt == 0:
        x1 = -b/(2*a)
        print('此方程有一个解：%s' % x1)
        return x1
    else:
        print('此方程无解。')

# a = int(input('请输入a:'))
# b = int(input('请输入b:'))
# c = int(input('请输入c:'))
# quadratic(a,b,c)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')