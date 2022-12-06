def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def pa(n):
    t=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==t:
        return True
    else:
        return False
n=int(input())
if n>=10 and n<=10000:
    for i in range(n+1,999999):
        if prime(i) and pa(i):
            print(i)
            break