n=int(input())

a=[]
b=[]
c=[]

for i in range(n):
    s_list=input().split()
    a=int(s_list[0])
    b=int(s_list[1])
    c=int(s_list[2])
    if a+b>c:
    #Case #1: false
        print("Case #%d: true"%(i+1))
    else:
        print("Case #%d: false"%(i+1))





