t=('hello','good','python',1,2,3,4,5,6)
print(t[0],type(t))
print(t[0:9:2])
for i in range(len(t)):
    print(i+1,".",t[i])

#使用enumerate函数进行遍历
for i,  a in enumerate(t,1):
    print(i,"->",a)
for i,  a in enumerate(t,2):
    print(i,"->",a)
