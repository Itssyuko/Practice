#!/usr/bin/env python
#-*- coding:utf-8 -*-
def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    if len(L) == 1:
        return(L[0],L[0])
    Max = L[0]
    Min = L[0]
    for num in L:
        if num > Max:
            Max = num
        if num < Min:
            Min = num
    return (Min,Max)
    # 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
    print(findMinAndMax([]))
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
    print(findMinAndMax([7]))
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
    print(findMinAndMax([7, 1]))
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
    print(findMinAndMax([7, 1, 3, 9, 5]))
else:
    print('测试成功!')
