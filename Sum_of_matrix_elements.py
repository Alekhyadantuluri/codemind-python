m=int(input())
n=int(input())
c=0
for i in range(1,m+1,1):
    d=list(map(int,input().split()))
    for i in d:
        c+=i
print(c)
    