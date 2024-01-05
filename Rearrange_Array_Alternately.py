t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=0
    if n%2==0:
        d=n//2
    else:
        d=n//2+1
    for i in range(d):
        c=c+1
        if c<=n:
            b.append(a[-(i+1)])
        c=c+1
        if c<=n:
            b.append(a[i])
    print(*b)