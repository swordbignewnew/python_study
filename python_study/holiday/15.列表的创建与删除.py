#直接使用[]创建列表
'''list1=['e','hello',99]
print()
print(list1)'''

#使用内置list函数创建列表
'''list2=list('good good study,day day up')
print(list2)
list3=list(range(1,10,3))
print(list3)'''

#列表是序列的一种，对序列的加乘同样适用
'''print(list3+list2+list1)
print(list3*2)
print(list2.index("o"))
print(list2.count("d"))'''

#列表的遍历
'''s=["hapyy","hhh","114514"]
for it in s:
    print(it)
print("-"*45)
for i in range(0,len(s)):
    print(i,"->",s[i])'''