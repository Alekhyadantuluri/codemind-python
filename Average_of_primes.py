def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
s=[]
for i in d:
    if prime(i):
        s.append(i)
a=sum(s)/len(s)
print('%.2f'%a)
