n=int(input())
d=list(map(int,input().split()))
if len(d)%2==0:
    print(*d)
else:
    d.append(0)
    print(*d)