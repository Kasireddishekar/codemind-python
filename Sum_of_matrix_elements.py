a=int(input())
b=int(input())
d=[]
s=0
for i in range(a):
    c=list(map(int,input().split()))
    d.append(c)
for j in range(a):
    for k in range(j,j+1):
        for l in range(b):
            s=s+d[k][l]
print(s)
    
