 #while 加冒号

#今天是否休息循环问
'''study_day=input("whether have classes today? yes or no\n")
while study_day=="yes":
    print("good good study,day day up")
    study_day=input("whether have classes today? yes or no\n")
    while study_day=="no":
        print("you should study everyday! so don't be lazy!")
        study_day = input("whether have classes today? yes or no\n")
while study_day=="no":
    print("you should study everyday! so don't be lazy!")
    study_day=input("whether have classes today? yes or no\n")
    while study_day=="yes":
        print("good good study,day day up")
        study_day = input("whether have classes today? yes or no\n")
if  study_day!="no" or "yes":
    print("just have yourself a good time")'''

#1-100循环加
'''s=0
i=1
while i<=100:
    s+=i
    i+=1
else:
    print(s)
print(s)
'''

#用户登录系统，给三次输入密码的机会
'''i=3
key=input("plesae input your keyword:")
while key!="143067":
    i-=1
    print("your keyword is wrong, you only have",i,"chance,be careful!")
    key = input("plesae input your keyword:")
    if i==1:
        print("you can't login in")
        break
while key=="143067":
     print("welcome to the system!")
     break'''