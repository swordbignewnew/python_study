t=(item for item in  range(10))#创建的为一个生成器对象
print(t,type(t))
#转化为tuple类型
'''t=tuple(t)
print(t,type(t))'''
#for循环遍历
'''for i in t:
    print(i)'''
#__next__()方法,每次取元组中的后一位元素，为抽取，不放回
for i in range(10):
    print(t.__next__())
print("-"*40)
for i in t:
    print(i)
print("-"*40)
print(tuple(t))


