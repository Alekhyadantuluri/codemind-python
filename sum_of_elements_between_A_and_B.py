n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in d:
    if a<=i and b>=i:
        s+=i
print(s)