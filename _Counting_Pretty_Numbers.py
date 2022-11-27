def rev(n):
    while n:
        r=n%10
        break
    return r
n=int(input())
for i in range(1,n+1):
    m,n=map(int,input().split())
    c=0
    for i in range(m,n+1,1):
        if rev(i)==2 or rev(i)==3 or rev(i)==9:
            c+=1
    print(c)
    
    