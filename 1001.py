'''
Author: h4m5t
Date: 2021-01-19 16:43:01
LastEditTime: 2021-01-19 16:43:01
'''
n=int(input())
t=0
while n!=1:
    if n%2==0:
        n=n/2
        t+=1
    else:
        n=((n*3)+1)/2
        t+=1
print(t)
       
        
    