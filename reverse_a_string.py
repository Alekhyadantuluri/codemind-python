s=input()
d=[]
a=''
for i in range(len(s)):
    d.append(s[i])
d.reverse()
for i in range(len(d)):
    a+=str(d[i])
print(a)