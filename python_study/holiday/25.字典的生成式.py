import random

dictionary={i:random.randint(1,100) for  i in range(1,5)}
print(dictionary)

list1=[1,2,3,4]
list2=['happy','teru','fantastic','moty']
dictionary={key:value for key,value in zip(list1,list2)}
print(dictionary)
dictionary=zip(list1,list2)
print(dict(dictionary))