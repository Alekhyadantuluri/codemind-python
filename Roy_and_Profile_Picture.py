l=int(input())
n=int(input())
for i in range(n):
    w,h=map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w==h and w>=l and h>=l:
        print("ACCEPTED")
    else:
        print("CROP IT")
        
    