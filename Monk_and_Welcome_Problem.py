n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            c=a[i]+b[j]
            break
    print(c,end=" ")
        
        