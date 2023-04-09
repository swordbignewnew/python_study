#数字置换
'''a=1
b=2
c=3
a,b,c=c,a,b
print(a,b,c)'''

#身高预测
import random

'''father_height=eval(input("please input father's height"))
mother_height=eval(input("please input mother's height"))
son_height=(mother_height+father_height)*0.54
print("son's height maybe is:",round(son_height,2))'''

#判断闰年
'''year=eval(input("please input the year:"))
if year%400==0 or (year%4==0 and year%100!=0):
    print("是闰年！")
else:
    print("不是闰年！")'''

#模拟10086查询功能
'''print("--------10086自助查询系统------------")
print("1.查询当前余额:")
print("2.查询当前剩余余量:")
print("3.查询当前通话剩余时间:")
print("0.退出系统")
choice=eval(input("请输入你的选项："))
while choice!=0:
    if choice==1:
        print("当前余额为：202！")
        choice_2=input("是否还要继续查询 yes or no?")
        if choice_2=="yes":
            choice = eval(input("请输入你的选项:"))
            continue
        if choice_2=="no":
            print("结束查询！")
            break
    if choice==2:
        print("剩余流量为114514G！")
        choice_2 = input("是否还要继续查询 yes or no?")
        if choice_2 == "yes":
            choice = eval(input("请输入你的选项:"))
            continue
        if choice_2 == "no":
            print("结束查询！")
            break
    if choice==3:
        print("剩余通话时间还有114514分钟！")
        choice_2 = input("是否还要继续查询 yes or no?")
        if choice_2 == "yes":
            choice = eval(input("请输入你的选项:"))
            continue
        if choice_2 == "no":
            print("结束查询！")
            break
if choice==0:
    print("查询结束！")'''

#猜数游戏
'''import  random
k=random.randint(1,100)#在1-100之间产生随机数
i=0
s=eval(input("请输入你猜测的数字！"))
while s!=k:
    if s<k:
        print("你猜小了")
        s = eval(input("请输入你猜测的数字！"))
        i+=1
        continue
    if s>k:
        print("你猜大了")
        s = eval(input("请输入你猜测的数字！"))
        i+=1
        continue
if s==k:
    i+=1
    print("恭喜你，猜对了!一共猜了",i,"次！")'''

#石头剪刀布小游戏
'''user_grade=0
robot_grade=0
robot=random.randint(1,3)
user_choice=eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
while user_choice==1 or user_choice==2 or user_choice==3:
    if user_choice==robot:
        print("平局！")
        robot = random.randint(1, 3)
        user_choice=eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
        continue
    if user_choice==1 and robot==3:
        print("你出剪刀，电脑玩家出布\n恭喜你获胜！得分加一！")
        user_grade+=1
        robot = random.randint(1, 3)
        user_choice = eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
        continue
    if user_choice==1 and robot==2:
        print("你出剪刀，电脑玩家出石头\n很遗憾，你输了！电脑玩家得分加一！")
        robot_grade+=1
        robot = random.randint(1, 3)
        user_choice = eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
        continue
    if user_choice==2 and robot==1:
        print("你出石头，电脑玩家出剪刀\n恭喜你获胜！得分加一！")
        user_grade += 1
        robot = random.randint(1, 3)
        user_choice = eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
        continue
    if user_choice==2 and robot==3:
        print("你出石头，电脑玩家出布\n很遗憾，你输了！电脑玩家得分加一！")
        robot_grade += 1
        robot = random.randint(1, 3)
        user_choice = eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
    if user_choice==3 and robot==1:
        print("你出布，电脑玩家出剪刀\n很遗憾，你输了！电脑玩家得分加一！")
        robot_grade += 1
        robot = random.randint(1, 3)
        user_choice = eval(input("请输入：1.剪刀 2.石头 3.布 4.结束\n"))
        continue
    if user_choice==3 and robot==2:
        print("你出布，电脑玩家出石头\n恭喜你获胜！得分加一！")
        user_grade += 1
        robot = random.randint(1, 3)
        user_choice = eval(input("请输入1.剪刀 2.石头 3.布 4.结束\n"))
        continue
if user_choice==4:
    print("游戏结束！\n你的得分为：", user_grade, "\n电脑玩家得分为：", robot_grade)
    if user_grade>robot_grade:
        print("你获得胜利！")
    elif user_grade==robot_grade:
        print("平局！")
    else:
        print("电脑玩家获得胜利！")
else:
    print("退出游戏！\n你的得分为：", user_grade, "\n电脑玩家得分为：", robot_grade)
    if user_grade > robot_grade:
        print("你获得胜利！")
    elif user_grade == robot_grade:
        print("平局！")
    else:
        print("电脑玩家获得胜利！")'''

#千年虫
'''list1=[80,89,90,98,00,99]
list2=[]
for item in list1:
    if item!=00:
        item+=1900
        list2.append(item)
    else:
        item+=2000
        list2.append(item)
print(list1)
print(list2)
print('-'*40)

print(list1)
for it in range(0,len(list1)):
    if list1[it]!=0:
        list1[it]+=1900
    else:
        list1[it]+=2000
print(list1)
for it in range(0,len(list1)):
    if list1[it]!=0:
        list1[it]='19'+str(list1[it])
    else:
        list1[it]='200'+str(list1[it])
print(list1)
'''

#京东购物流程
'''list1=[]
for i in range(0,3):
    list1.append(input("请输入需要入库的商品编号与名称："))
print("库中已有编号及商品为：")
for i in range(0,5):
    print(list1[i])
cage=[]
count=0
while 1:
    count+=1
    num = input("请输入需要购买的商品编号,输入back结束购物：")
    for i in list1:
        if num==i[0:4]:
            count=0
            cage.append(i)
            print("您的商品已经添加到购物车！")
            break
    if count!=0:
        print("您选的商品现在并不存在！")
    if num=="back":
        break
print("你的购物车已有商品为：")
cage.sort()
for i in range(0,len(cage)):
    print(cage[i])'''

#12306购票流程
'''list1={'G1569':['\t\t北京南-天津南','  18:05','     18:39','   00:34'],
       'G1567':['\t\t北京南-天津南','  18:15','     18:49','    00:34'],
       'G8917':['\t\t北京南-天津西','  18:20','     19:19','    00:59'],
       'G203' :['\t\t北京南-天津南','  18:35','     19:09','    00:34']}
print('车次',' \t\t出发站-到达站',' 出发时间','到达时间','历时',)
for first in list1.keys():
    print(first,end='')
    for second in list1.get(first):
        print(second,end=" ")
    print()
ticket=input("请输入要购买的车次：")
name=input("请输入乘车人的姓名(如果为多人请用逗号隔开！)：")
flag=list1.get(ticket)
if flag:
    print("您已购买了",ticket,"次列车",flag[0],flag[1],'开请',name,"按时兑换车票乘车")
else:
    print("车次不存在！")'''

#模拟手机通讯录
'''card=set()
count=0
while 1:
    count+=1
    friend=input("请输入第"+str(count)+"朋友的名称和电话号码(输入0停止输入):")
    if friend=='0':
        break
    card.add(friend)
for it in card:
    print(it)'''


