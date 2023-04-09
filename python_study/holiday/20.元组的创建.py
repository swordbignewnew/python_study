#直接创建
t=("hello","world",8,7,9)
print(t)
#使用内置tuple函数创建
t=tuple("helloworld")
print(t)
t=tuple([1,2,3,45,6])
print(t)
t=tuple(range(10))
print(t)
'''
元组是序列的一种，
对序列的操作同样对元组适用
'''
del t#删除元组