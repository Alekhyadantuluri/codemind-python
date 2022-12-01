import math
n=int(input())
d=list(map(int,input().split()))
s=[]
for i in d:
    m=int(math.log10(i)+1)
    s.append(m)
s.sort()
s.reverse()
print(s.count(s[0]))