s=input()
d=s.split()
a=[]
for i in d:
    a.append(len(i))
print(max(a))