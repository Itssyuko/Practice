#/usr/bin/env python
#-*- coding: utf-8 -*-
#when u think of this problem,first u should figure out how many cases are there
# 1.no space in this string
# 2. have some spaces at the beginning or some spaces at the end of the string,or both
# 3. the string consists of a number of spaces
def trim(s):
   flag = 1
   while flag == 1:
       if s[:1] == ' ':
           s = s[1:]
        elif s[-1:] == ' ':
            s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')