n=int(input())
s=[]
while n>0:
    r=n%10
    s.append(r)
    n=n//10
c=[]
for i in s:
    if i not in c:
        c.append(i)
if s==c:
    print("Unique Number")
else:
    print("Not Unique Number")