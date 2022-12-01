def c(n):
    s=0
    if n<0:
        n=abs(n)
    while n>0:
        r=n%10
        s+=1
        n=n//10
    return s
n=int(input())
d=list(map(int,input().split()))
s=[]
for i in d:
    s.append(c(i))
for i in d:
    if max(s)==c(i):
        print(i,end=" ")
    