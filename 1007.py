#查找小于n的d=2的质数对
n=int(input())

#判断是否是质数
def judge(number):
    if number<=1:
        return False
    if number==2:
        return True
    for i in range(2,int(number**(0.5))+1):
        if not number%i:
            return False
            
    return True

sum=0
for num in range(5,n+1,2):
    if judge(num) and judge(num-2):
        #print(num,num-2)
        sum+=1
print(sum)



