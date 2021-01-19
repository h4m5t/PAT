'''
Author: h4m5t
Date: 2021-01-19 18:18:38
LastEditTime: 2021-01-19 23:13:05
'''
n=int(input())

#读入数据
data=[]
for i in range(n):
    t=input()
    data.append(t)


#对字符串s进行判断
def judge(s):
    #先判断是否仅有PAT
    flag=0
    for i in s:
        if i!='P' and i!='A' and i!='T':
            flag=0
            print("NO")
            return
    #PAT
    if s=='PAT':
        print("YES")
        return
    if len(s)<3:
        print("NO")
        return


    #xPATx
    #aPbTc
    #设a,b,c,分别为P之前，中间，T之后'A'的个数
    a=0
    b=0
    c=0
    length=len(s)
    for i in range(length):
        if s[i]!='P':
            a=a+1
        else:
            break
    s=s[a+1:]
    #print(s)

    for i in range(len(s)):
        if s[i]!='T':
            b=b+1
        else:
            break

    c=length-a-b-2
    #以下为归纳重点
    if c==a*b:
        print("YES")
        return
    else:
        print("NO")
        return
    
        

#有n个字符串需要判断
for i in range(n):
    judge(data[i])
