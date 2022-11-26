n=int(input())
d=list(map(int,input().split()))
b=set(d)
s=0
for i in b:
    if i%2:
        s+=i
print(s)