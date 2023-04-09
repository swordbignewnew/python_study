#输出长方形
'''for i in range(1,4):
 for j in range(1,5):
        print("*",end="")
    print()'''
#print("-----------------------")
'''i=0
cout=0
while i<=4:
    print("*",end="")
    i+=1
    if i==4 and cout<3:
        cout+=1
        i=0
        print()
    if cout==3:
        break'''

#输出直角三角形
'''for s in range(1,6):
    for k in range(1,s+1):
        print("*",end="")
    print()'''

#输出倒直角三角形
'''for s in range(1,6):
    for k in range(1,7-s):
        print("*",end="")
    print()'''

#输出等腰三角形
'''for s in range(1,6):
    for k in range(1,2*s):
        j=5-s
        while j>0:
            print(" ",end="")
            j-=1
        else:
            break
    for m in range(1,2*s):
        print("*",end="")
    print()'''