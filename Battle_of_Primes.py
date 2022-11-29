def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
s=m+n
for i in range(s+1,99999):
    if prime(i):
        a=i
        break
print(i-s)