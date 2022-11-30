import math
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
t=n
s=0
d=int(math.log10(n)+1)
while  n>0:
    r=n%10
    if prime(r):
        s+=1
    n=n//10
if prime(t):
    if s==d:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")