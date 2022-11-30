n=int(input())
d=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    if i%2==0 and d[i]%2==0:
        s+=1
    if d[i]%2==0:
        c+=1
if s==c:
    print("True")
else:
    print("False")