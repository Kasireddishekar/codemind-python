n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=[]
for i in range(n-1,(n//2)-1,-1):
    b.append(a[i])
for j in range(0,(n//2)):
    c.append(a[j])
d=b+c
print(*d)
    
    