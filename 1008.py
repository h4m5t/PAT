#有n 个数的数组循环右移M位
n,m=map(int,input().split())

m=m%n
number=input().split()

def move(list):
    tmp=list[-1]
    for i in range(len(list)-1,0,-1):
        #print(i)
        list[i]=list[i-1]
    list[0]=tmp
    #print(list)
    
    return list
for i in range(m):
    move(number)

print(' '.join(str(i) for i in number))