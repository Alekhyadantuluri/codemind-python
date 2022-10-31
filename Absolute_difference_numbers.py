import math
n,m=map(int,input().split())
d=int(math.log10(n)+1)
i=n%math.pow(10,m)
j=n//math.pow(10,d-m)
print(int(abs(i-j)))

    