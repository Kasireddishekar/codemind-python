n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    d=a[i]+b[i]
    c.append(d)
print(*c)