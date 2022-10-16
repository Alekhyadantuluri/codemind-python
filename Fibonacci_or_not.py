n=int(input())
a=0
b=1
c=a+b
d=0
while n:
    a=b
    b=c
    c=a+b
    if c==n:
        d=1
    elif c>=n:
        break
        d=0
if d==1:
    print("True")
else:
    print("False")