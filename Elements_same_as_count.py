n=int(input())
d=list(map(int,input().split()))
s=[]
for i in d:
    if d.count(i)==i:
        if i not in s:
            s.append(i)
if len(s)==0:
    print("-1")
else:
    print(*s)