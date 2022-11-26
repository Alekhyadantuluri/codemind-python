n=int(input())
d=list(map(int,input().split()))
b=set(d)
c=0
for i in b:
    if i%2==0:
        c+=1
print(c)
    