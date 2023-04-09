#集合属于序列的一种

#使用{}直接创建集合
import random

s={10,20,30,40}
print(s)
s={"happy",'teru','try','gyt'}
print(s,type(s))

#直接创建s={}为字典
s={}
print(type(s))
#使用set()创建空集合
s=set()
print(type(s))

#使用set（）函数进行创建

s=set("hapyypython")#集合中不允许有重复的元素
print(s)
s=set([10,20,30])
print(s)
s=set(random.randint(1,10) for i in  range(5))
print(s)
print('max:',max(s))
print('max:',min(s))
print('len:',len(s))
print(9 in s)
print(1 in s)
del  s
