n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=int(input())
s=0
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            if a[i]<=c and b[j]>=c:
                s+=1
print(s)
                
            
