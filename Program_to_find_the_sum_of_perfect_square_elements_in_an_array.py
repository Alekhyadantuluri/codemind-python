import math
n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    s=int(math.sqrt(i))
    m=s*s
    if i==m:
        c+=i
print(c)
    