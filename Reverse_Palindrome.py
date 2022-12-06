def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
def pa(n):
    if rev(n)==n:
        return True
    else:
        return False
n=int(input())
while True:
    n=n+rev(n)
    if pa(n):
        print(n)
        break
    