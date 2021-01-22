n=int(input())
name=[0]*n
num=[0]*n
score=[0]*n

for i in range(n):
    name[i],num[i],score[i]=input().split()
    score[i]=int(score[i])

themax=score[0]
themin=score[0]
index_max=0
index_min=0

for i in range(n):
    if score[i]>themax:
        themax=score[i]

    if score[i]<themin:
        themin=score[i]

for i in range(n):
    if score[i]==themax:
        index_max=i
    if score[i]==themin:
        index_min=i

print(name[index_max],num[index_max])
print(name[index_min],num[index_min])



    
    