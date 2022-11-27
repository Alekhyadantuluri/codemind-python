import math
n=int(input())
for i in range(1,n+1,1):
    m=int(input())
    s=int(math.sqrt(m))
    a=s*s
    if m==a:
        print("True")
    else:
        print("False")
