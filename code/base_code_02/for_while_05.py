# -*- coding: utf-8 -*-
'''
# 循环
'''

# for in

for item in ['a', 'b', 'c']:
    print(item)
print('------------------')

SUM = 0
for item in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    SUM += item
print(SUM)
## 有一个range()函数可生成整数序列

SUM2 = 0
for item in list(range(11)):
    SUM2 += item
print(SUM2)

SUM3 = 0
print(list(range(10, 20, 3)))
# 从10 到 25 间隔为5
for item in list(range(10, 25, 5)):
    SUM3 += item
print(SUM3)
print('------------------')
