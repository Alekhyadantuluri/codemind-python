m=int(input())
d=list(map(int,input().split()))
n=int(input())
s=0
for i in d:
    if i<=n:
        s+=i
print(s)
