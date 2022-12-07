n=int(input())
d=list(map(int,input().split()))
a=[]
b=[]
for i in d:
    if i not in a:
        a.append(i)
for i in a:
    b.append(i)
    b.append(d.count(i))
print(*b)