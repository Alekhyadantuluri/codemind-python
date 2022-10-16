n=int(input())
s=n*n
temp=s
sum=0
while s:
    d=s%10
    sum=sum+d
    s=s//10
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")
    
