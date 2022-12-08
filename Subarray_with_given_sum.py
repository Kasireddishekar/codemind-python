T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    for i in range(a):
        for j in range(i+1,a+1):
            s=0
            for k in range(i,j):
                s=s+c[k]
            if s==b:
                print(i+1,j)
                break
        if s==b:
            break
    else:
        print(-1)