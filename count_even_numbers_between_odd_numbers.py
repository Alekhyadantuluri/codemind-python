n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(len(d)-2):
    if d[i]%2!=0 and d[i+2]%2!=0 and d[i+1]%2==0:
        c+=1
print(c)