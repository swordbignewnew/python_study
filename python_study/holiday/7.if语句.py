#if语句后要加冒号
'''x=eval(input("请输入一个数:"))
if x%2:
    print("输入的数为奇数")
else:
    print("输入的数为偶数")


grade=eval(input("please input your grade:"))
if grade>100 or grade<0:
    print("pass your wind")
elif grade<=100 and grade>=90:
    print("very good")
elif 90>grade>=80:
    print("good")
else:
    print("just so so")'''

sentence=input("whether have you drank? please say yes or no\n:")
if sentence=="yes":
    amout=eval(input("have many bottles have you drank?\n:"))
    if amout>=20:
        print("you have drank a lot,please don't drive")
    elif 20>amout>=10:
        print("you have drank , so it is better not to drive ")
    elif 10>amout:
        print("you have drank a little,you can drive slowly")
elif sentence=="no":
    print("you can drive,but be careful")