a,b=map(int,input().split())
c=list(map(int,input().split()))
d=c.copy()
e=[]
for i in range(b):
    e.append(c[i])
    d.remove(c[i])
d.extend(e)
print(*d)
    
    
