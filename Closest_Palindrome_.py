def palin(n):
    s=0
    t=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==t:
        return True
    else:
        return False
n=int(input())
for i in range(n-1,0,-1):
    if palin(i):
        a=i
        break
for i in range(n+1,999999):
    if palin(i):
        b=i
        break
if n-a<b-n:
    print(a)
elif n-a==b-n:
    print(a,b)
else:
    print(b)