def c(n):
    s=0
    while n>0:
        r=n%10
        s+=1
        n=n//10
    return s
n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    a.append(c(i))
a.sort()
print(a.count(a[0]))

    