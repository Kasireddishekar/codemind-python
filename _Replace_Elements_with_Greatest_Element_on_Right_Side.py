n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    b=[]
    for j in range(i+1,n):
        b.append(a[j])
    if i==n-1:
        print(-1)
    else:
        print(max(b),end=" ")
        