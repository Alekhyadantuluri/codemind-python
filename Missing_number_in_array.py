n=int(input())
for i  in range(1,n+1,1):
    m=int(input())
    d=list(map(int,input().split()))
    for i in range(1,m+1,1):
        if i not in d:
            print(i)