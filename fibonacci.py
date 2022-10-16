n=int(input())
a=0
b=1
c=a+b
print(a,b,end=" ")
for i in range(1,n-1,1):
    print(c,end=" ")
    a=b
    b=c
    c=a+b