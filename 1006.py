n=int(input())
#n<1000
#求出百位，十位，个位

bw=n//100
sw=(n-(bw*100))//10
gw=n%10

print(bw,sw,gw)
for i in range(bw):
    print('B',end='')
for i in range(sw):
    print('S',end='')
for i in range(gw):
    print(i+1,end='')