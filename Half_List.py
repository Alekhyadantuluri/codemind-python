n=int(input())
d=list(map(int,input().split()))
s=len(d)//2
for i in range(len(d)-1,s-1,-1):
    print(d[i],end=" ")
for i in range(s):
    print(d[i],end=" ")