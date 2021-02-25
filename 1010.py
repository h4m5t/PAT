a=list(map(int,input().split()))
res=[]
length=len(a)

for i in range(0,length,2):
    x=a[i]*a[i+1]
    y=a[i+1]-1
    if x:
        res.append(x)
        res.append(y)
if not len(res):
    print("0 0")
else:
    res=map(str,res)
    print(' '.join(res))
