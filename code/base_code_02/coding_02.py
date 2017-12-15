# -*- coding: <encoding name> -*-
# coding:utf-8
# 上方两种注释方式，第一种适用性更广
'''
# 编码
'''

# ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))
print('-------------------------')

# chr()函数把编码转换为对应的字符
print(chr(65))
print(chr(20013))
print('\u4e2d')
print('-------------------------')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示

BYTE1 = b'AAA'
print(BYTE1)
print('AAA'.encode('ascii'))
print('AAA'.encode('utf-8'))
print('-------------------------')

# 反过来 字节流(bytes)转str
print(b'AAA'.decode('utf-8'))
print(b'\xe4\xb8\xad'.decode('utf-8'))
# print(b'\xe4\xb8\xad'.decode('ascii')) 中文超出ascii报错，可使用errors='ignore'忽略报错部分：
print(b'\xe4\xb8\xad'.decode('ascii', errors='ignore'))
print('-------------------------')

# len
# 对于str 获取字符数
print(len('aaabbb'))
print(len('大蛇'))
# 对于btyes 获取字节数
print(len(b'aaabbb'))
print(len('大蛇'.encode('utf-8')))
print('-------------------------')

# 格式化输出

'''
  %d	整数
  %f	浮点数
  %s	字符串
  %x	十六进制整数
'''

print('%.2f' % 3.1415926)
# %3d 应该是%3d长为3
# %03d 应该是%03d 长为3并用0补全
print('%3d-%03d' % (333, 1))
STR = ('%d-%0d' % (33, 1))
print(STR)
# 只在格式化整数和浮点数时可指定整数与小数的位数和是否补0和
print('%3s' % ('中文的长度'))

# 另一种格式化输出 format()

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('-------------------------')

LAST_NUM = 72
NOW_NUM = 85
K = (NOW_NUM - LAST_NUM)/LAST_NUM * 100
print('去年成绩:%d，今年成绩:%d，提高了%.1f%%' % (LAST_NUM, NOW_NUM, K))
print('去年成绩:{0}，今年成绩:{1}，提高了{2:.1f}%'.format(LAST_NUM, NOW_NUM, K))
