# -*- coding: <encoding name> -*-
# coding:utf-8
# 上方两种注释方式，第一种适用性更广
'''
# 编码
'''

# ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))

# chr()函数把编码转换为对应的字符
print(chr(65))
print(chr(20013))
print('\u4e2d')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示

BYTE1 = b'AAA'
print(BYTE1)
print('AAA'.encode('ascii'))
print('AAA'.encode('utf-8'))

# 反过来
print(b'AAA'.decode('utf-8'))
print(b'\xe4\xb8\xad'.decode('utf-8'))
# print(b'\xe4\xb8\xad'.decode('ascii')) 中文超出ascii报错
