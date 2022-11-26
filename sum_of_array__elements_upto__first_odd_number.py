m=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    if i%2==0:
        s+=i
    else:
        break
print(s)

