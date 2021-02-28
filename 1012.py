#输出A1~A5
num=list(map(int,input().split()))
#n表示数字的个数
n=num[0]

a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
#利用5个数组保存5种数
for i in range(1,n+1):
    if num[i]%5==0:
        a1.append(num[i])
    elif num[i]%5==1:
        a2.append(num[i])
    elif num[i]%5==2:
        a3.append(num[i])
    elif num[i]%5==3:
        a4.append(num[i])
    elif num[i]%5==4:
        a5.append(num[i])
A1=0
if a1:
    for number in a1:
        if number%2==0:
            A1+=number
A2=0
if a2:
    flag=1
    for number in a2:
        if flag==1:
            A2=A2+number
        elif flag==-1:
            A2=A2-number
        
        flag=-flag

A3=len(a3)

if a4:
    A4=sum(a4)/len(a4)

if a5:
    A5=max(a5)

if a1 and A1!=0:
    print(A1,end=" ")
else:
    print("N",end=" ")

if a2:
    print(A2,end=" ")
else:
    print("N",end=' ')
if a3:
    print(A3,end=" ")
else:
    print("N",end=" ")
if a4:
    print("%.1f"%A4,end=" ")
else:
    print("N",end=" ")
if a5:
    print(A5,end="")
else:
    print("N",end='')

























































    





































    

