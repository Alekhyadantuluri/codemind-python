m=int(input())
temp=m
rev=0
while m:
    d=m%10
    rev=(rev*10)+d
    m=m//10
if rev==temp:
    print("True")
else:
    print("False")

    