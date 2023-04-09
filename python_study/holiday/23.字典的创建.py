dictionary={1: 'good', 2: 'study', 3: 'up'}
print(dictionary)
#key值相同，后来的对之前的进行覆盖
dictionary={1: 'good', 2: 'study', 3: 'up',1:"happy"}
print(dictionary)

#通过zip函数zip(lis1,lis2)进行字典的创建,创建的为zip对象
lis1=[1,2,3]
lis2=["happy","every","day"]
lis3=zip(lis1,lis2)
print(lis3,type(lis3))
print(list(lis3))
print(dict(lis3))

d=dict(happy=1,egg=2)
print(d)

t=(10,20,30)
print({10:t})

print("max",max(lis1))
print("min" ,min(lis1))
print("len", len(lis2))

#删除d
del  d

