def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(1,n+1):
    s=int(input())
    for i in range(s,0,-1):
        if prime(i):
            a=i
            break
    for i in range(s,999999):
        if prime(i):
            b=i
            break
    if s-a>b-s:
        print(b)
        
    else:
        print(a)
        