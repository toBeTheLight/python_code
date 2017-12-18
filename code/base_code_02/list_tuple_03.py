# -*- coding: <encoding name> -*-
'''
# list列表和tuple元组
'''

'''
 python 中的 list **子项结构**比较像 js 中的 array ，可类型不同。
 而python中的 array 就是正经 array。
'''

# list:列表 有序集合

CLASSMATES = ['0', '1']
print(CLASSMATES)
print('------------------')
## 取长
LENGTH = len(CLASSMATES)
print(LENGTH)
print('------------------')

## 索引取值
print(CLASSMATES[0])
### print(CLASSMATES[2]) 索引超出报错，错误引用
print('------------------')
### 同样索引可取负值
print(CLASSMATES[-2])
print('------------------')
## 添加元素
CLASSMATES.append('2')
print(CLASSMATES)
print('------------------')
## 插入元素
CLASSMATES.insert(5, 3)
print(CLASSMATES)
### 插入位置索引超出最大索引会取最大索引
print(len(CLASSMATES))
print('------------------')
## 删除元素
print(CLASSMATES.pop(-1))
### 不传索引默认队尾
print(CLASSMATES.pop())
print(CLASSMATES)
print('------------------')
## 索引赋值
CLASSMATES[1] = 'test'
### CLASSMATES[100] = 'test' 很明显这个会报错。这就是与js数组的不同了。
print(CLASSMATES)
print('------------------')


# tuple 直接子项不可变的“列表” “只能读值”

## tuple 的 元素的指向是不可变的。如同用js中的const定义了子项的效果
TUPLE1 = (1, 2, 3)
TUPLE2 = (4, 5, [5, 6])
## 只有一项时要加,
TUPLE3 = (8,)
# TUPLE1[1] = 'x' 不能这么做
TUPLE2[2][1] = 'x'# 可以这么做
print(TUPLE2)
