a=int(input())
for i in range (1,a):
    b=i*(i+1)
    if b==a:
        break
if b==a:
    print("YES")
else:
    print("NO")