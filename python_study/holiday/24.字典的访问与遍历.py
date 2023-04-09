dictionary={1: 'good', 2: 'study', 3: 'up'}
print(dictionary)
print(dictionary[1])
for i in range(1,4):
    print(i,"-->",dictionary[i])
print(dictionary.get(1))
print(dictionary.get(4))
print(dictionary.get(4,"can't find"))

for i in dictionary.items():
    print(i)
for key,i in dictionary.items():
    print(key,i)

#keys()获取编号元素，values()获取数值元素
print(dictionary.keys())
print(dictionary.values())
#取一个指定的key-value并删除
print('-'*40)
print(dictionary.pop(1,"不存在"))

print(dictionary.keys())
#随机取一个key-value对后删除
print('-'*40)
print(dictionary.popitem())

print(dictionary.keys())
#清除所有key-value对
print('-'*40)
print(dictionary.clear())

print(dictionary.keys())
#在字典中添加key-value对
print('-'*40)
dictionary[4]='happy'
print(dictionary)
