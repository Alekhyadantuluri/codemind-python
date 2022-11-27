n=int(input())
d=list(map(int,input().split()))
for i in d:
    if d.count(i)>n//2:
        c=i
print(c)