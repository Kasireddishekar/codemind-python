a=int(input())
n=list(map(int,input().split()))
c=[]
d=[]
for i in n:
    if i==0:
        c.append(i)
    else:
        d.append(i)
c.extend(d)
print(*c)