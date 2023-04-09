a={1,3,59,95,66}
b={2,3,45,68,95,59}

#交集&
print(a&b)
#并集|
print(a|b)
#添加集合元素add（）,不能直接print(a.add(X))
a.add(2)
print(a)
#删除集合之中的元素remove（），不能直接print（remove（X)）
a.remove(3)
print(a)
#清除所有元素clear()
'''a.clear()
print(a)'''
#集合的遍历
for it in a:
    print(it,end=" ")
print("")
for key, it in enumerate(a):
    print(key,'-->',it,end=" ")
