'''for i in "happy":
    print(i)
#range函数，(n,m).产生一个n-m的整数，包含n，不包含m
result=0
for i in range(5,15):
    if i%2:
        print(i,"为奇数")
    result+=i
print(result)'''

#100-999之间的水仙花数
'''eg:
153
3*3*3+5*5*5+1*1*1=153
153为水仙花数
'''

'''for i in range(100,1000):
    g=i%10
    s=(i//10)%10
    q=i//100
    if g**3+s**3+q**3==i:
        print("yes",i,"it is a wonderful data")
'''
'''print(153//100)
print(153//10%10)'''
s=0
for i in range(1,11):
    s+=i
else:
    print(s)

