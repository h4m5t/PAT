#找出中间的所有素数
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num=[0,2]
cnt=0

for i in range(3,150000,2):
    if is_prime(i):
        num.append(i)
        cnt+=1
    if cnt==10000:
        break

m,n=map(int,input().split())
tmp=0
for i in range(m,n+1):
    tmp+=1
    if tmp!=0 and tmp%10==0:
        print(num[i],end='\n')
    elif i==n:
        print(num[i],end='')
    else:
        print(num[i],end=' ')
    
