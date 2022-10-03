def rev(n):
    min=0
    while n:
        d=n%10
        n=n//10
        if d>min:
            min=d
    return min

n=int(input())
print(rev(n))
