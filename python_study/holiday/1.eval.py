#eval执行去掉引号的运算
s="3.14+3"
print(s,type(s))
x=eval(s)
print(x,type(x))
hello="i am happy"

age=eval(input("please input your age:"))
print(age,type(age))
#hello代表一个标识符
print(eval("hello"))
