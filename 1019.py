N=input().zfill(4)
def asc(N):#升序排列
    return(int(''.join(sorted(N))))
def desc(N):#降序排列
        return(int(''.join(sorted(N,reverse=True))))
while 1:
    if int(N)%1111==0:
        print('{} - {} = 0000'.format(N,N))
        break
    descn=str(desc(N)).zfill(4)
    ascn=str(asc(N)).zfill(4)
    N=str(desc(N)-asc(N)).zfill(4)
    print('{} - {} = {}'.format(descn,ascn,N))
    if N=='6174' : break