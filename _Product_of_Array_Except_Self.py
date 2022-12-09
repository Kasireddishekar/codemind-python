a=int(input())
b=list(map(int,input().split()))
c=b.copy()
p=1
for i in range(a):
    c.remove(b[i])
    l=len(c)
    for j in range(l):
        p=p*c[j]
    print(p,end=" ")
    c=b.copy()
    p=1
    
