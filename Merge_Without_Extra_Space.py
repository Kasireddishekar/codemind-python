T=int(input())
for i in range(0,T):
    x,y=map(int,input().split())
    P=list(map(int,input().split()))
    Q=list(map(int,input().split()))
    P.extend(Q)
    P.sort()
    print(*P)