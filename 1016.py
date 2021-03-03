#a,da,b,db=map(int,input().split())
a,da,b,db=input().split()


suma=0
for i in a:

    if da==i:
        suma+=1

sumb=0
for i in b:

    if db==i:
        sumb+=1




print(int(suma*da)+int(sumb*db))




