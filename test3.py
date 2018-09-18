#/usr/bin/env python
#-*- coding: utf-8 -*-
#when u think of this problem,first u should figure out how many cases are there
# 1.no space in this string
# 2. have some spaces at the beginning or some spaces at the end of the string,or both
# 3. the string consists of a number of spaces

def trim(s):
    length = len(s) 
    if length == 0:  # 如果s是空字符串，直接返回
        return s
    x = 0 
    while x < length:
        if s[x] == ' ':
            x = x + 1 #如果当前字符是空格，则取下一位验证
        else:
            break # 起始出现非空格字符，前面部分索引结束，跳出循环
    # if x == length:
    #     s = ''
        # return s
    while s[length - 1] == ' ': 
        # if length > x:
        length = length-1  #从尾部开始检索，如果当前是空格，则往前检索
        if length == 0:
            s = ''
            return s
    print(x,length)
    return s[x:length]


# Mark's
# def trim(s):
#     left = 0
#     right = len(s)-1
#     while left < right and right > 0:
#         if s[left] == ' ':
#             left = left + 1
#         if s[right] == ' ':
#             right = right - 1
#         if left > right:
#             s = '' 
#             return s
#         print(left,right)
#     return s[left:right]  #这是个死循环23333

# def trim(s):
#     l = len(s)
#     n = 0
#     x = 0
#     if l == 0:
#         return s
#     while n < l:
#         if s[n] == ' ':
#             n = n + 1
#         else:
#             print(n)
#             break
#     s2 = s[::-1] #把list倒序
#     while x < l:
#         if s2[x] == ' ':
#             x = x + 1
#         else:
#             print(x)
#             break
#     x = l - x
#     return s[n:x]

 
if trim('hello  ') != 'hello':
    print('测试失败!')
    print('1',trim('hello  '))
else:
    print('1测试成功!')
if trim('  hello') != 'hello':
    print('测试失败!')
    print('2',trim('  hello'))
else:
    print('2测试成功!')
if trim('  hello  ') != 'hello':
    print('测试失败!')
    print('3',trim('  hello  '))
else:
    print('3测试成功!')
if trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
    print('4',trim('  hello  world  '))
else:
    print('4测试成功!')
if trim('') != '':
    print('测试失败!')
    print('5',trim(''))
else:
    print('5测试成功!')
if trim('    ') != '':
    print('测试失败!')
    print('6',trim('    '))
else:
    print('6测试成功!')