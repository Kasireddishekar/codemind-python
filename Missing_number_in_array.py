T=int(input())
for i in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    k=N*(N+1)//2
    s=sum(a)
    res=k-s
    print(res)