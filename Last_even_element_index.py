n=int(input())
d=list(map(int,input().split()))
for i in range(n):
    if d[i]%2==0:
        s=i
print(s)