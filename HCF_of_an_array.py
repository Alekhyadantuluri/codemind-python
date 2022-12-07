n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if i%min(d)==0:
        c+=1
if c==len(d):
    print(min(d))
else:
    print("1")