# -*- coding: utf-8 -*-
'''
# 条件判断
'''

AGE = 18
if AGE < 14:
    print('u lose it')
# js里不能这么连着写，类型转来转去的结果就错了
elif 18 > AGE >= 15:
    print('u almost get it')
else:
    print('u get it')
print('-------------')

WEIGHT = input('输入体重')
## 同样input获得的是字符串
print(WEIGHT)
WEIGHT = int(WEIGHT)
print(WEIGHT)
if 18.5 > WEIGHT:
    print('过轻')
elif 25 > WEIGHT >= 18.5:
    print('正常')
elif 28 > WEIGHT >= 25:
    print('过重')
elif 32 > WEIGHT >= 28:
    print('肥胖')
else:
    print('严重肥胖')
