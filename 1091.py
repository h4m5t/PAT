m=int(input())
#k**2 * n 自守数
#判断k的位数

#数据的读入
num=[]
num=input().split(" ")


def judge(number):
    
    number_length=len(str(number))
    

    for i in range(1,10):
        #判断运算后的后length位
        if ((number**2)*i)%(10**number_length)==number:
            print(i,(number**2)*i)
            break
        if i==9:
            print("NO")
#解题
for i in range(m):
    judge(int(num[i]))
            


