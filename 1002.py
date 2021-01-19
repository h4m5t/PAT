'''
Author: h4m5t
Date: 2021-01-19 17:50:21
LastEditTime: 2021-01-19 18:17:26
'''
n=input()
#print(n)

Sum=0
for i in n:
    i=int(i)
    Sum=Sum+i

#print(Sum)
t=str(Sum)
length=len(t)
tmp=1

dict1={1:'yi',2:'er',3:'san',4:'si',5:'wu',6:'liu',7:'qi',8:'ba',9:'jiu',0:'ling'}

for i in t:
    i=int(i)
    if tmp==length:
        print(dict1[i])
    else:
        print(dict1[i],end=' ')
        tmp+=1


