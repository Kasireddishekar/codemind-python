n=int(input())
a=[]
s=0
for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(n):
    for k in range(n):
        if j==k or j==n-k-1:
            s=s+a[j][k]
print(s)
        
            
    