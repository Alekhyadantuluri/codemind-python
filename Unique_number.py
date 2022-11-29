n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
for i in l:
    if l.count(i)>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")