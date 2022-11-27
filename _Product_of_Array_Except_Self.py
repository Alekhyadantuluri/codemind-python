n=int(input())
d=list(map(int,input().split()))
s=1
for i in d:
    s=s*i
for i in d:
    print(s//i,end=" ")