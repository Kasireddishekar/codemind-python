n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
c=[]
for i in range(n):
    if i%2==1:
        c.append(a[i])
        c.append(a[i-1])
if n%2==1:
    c.append(a[n-1])
print(*c)
        