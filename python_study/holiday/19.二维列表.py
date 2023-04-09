#二维列表
'''lis=[  ["地点",'距离','    花费'],
        ['北京','30km','13540元'],
        ["上海",'100km','10000元'],
        ['云南','70km','12000元']
     ]
print(lis)
print("-"*45)
for first in lis:
    for second in  first:
        print(second,end="\t")
    print()
'''
#二维列表的生成
import random

lis=[[random.randint(0,100 ) for j in range(0,5)]for i in  range(0,4)]
for first in lis:
    for second in  first:
        print(second,end="   ")
    print()