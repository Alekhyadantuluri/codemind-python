def prime(n):
    if n==2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(n,0,-1):
    if prime(i):
        a=i
        break
for i in range(n,999999):
    if prime(i):
        b=i
        break
if n-a<b-n:
    print(n-a)
else:
    print(b-n)
        