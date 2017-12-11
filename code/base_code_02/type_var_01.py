'''
python 几种可直接处理的数据类型有
1. 整数
2. 浮点数
3. 字符串
4. 布尔值
5. 空值
'''
'''
# 1. 整数
'''
NUM1 = 1
# 同可声明进制数
NUM16 = 0x123
'''
# 2. 浮点数
'''
NUM3 = 0.123
NUM4 = 0.01e-11
NUM5 = 0.1e-12
print(NUM5)
'''
# 3. 字符串
'''
STR1 = 'abc'
STR2 = 'a\'b'
# r''引号中内容可默认不转义
STR3 = r'\b\n\a'
print(STR3)
# 3'可直接表示多行
STR4 = '''第一行
第二行
第三行'''
print(STR4)
'''
# 4. 布尔值
'''
# 与js不同的是要大写
BOOL1 = True
BOOL2 = False
# 注意python中没有 && || !
print(BOOL1 and BOOL2)
# 有的是 and -> &&  or -> ||  not -> !
print(BOOL1 == (not BOOL2))

'''
# 5.空值
'''
NONE = None
print(NONE)

'''
# 除此之外还有
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）
'''
