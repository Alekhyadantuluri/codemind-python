def c(n):
    if n==0:
        return 1
    s=0
    if n<0:
        n=abs(n)
    while n>0:
        r=n%10
        s+=1
        n=n//10
    return s
m,n=map(int,input().split())
d=list(map(int,input().split()))
a=0
for i in d:
    if c(i)==n:
        a+=1
print(a)