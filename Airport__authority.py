n=int(input())
m=[]
for i in range(1,n+1,1):
    i=int(input())
    m.append(i)
a=int(input())
c=0
for i in m:
    if i>a:
        c+=2
    else:
        c+=1
print(c)
        