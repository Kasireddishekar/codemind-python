T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    for i in range(b):
        c.insert(0,c[-1])
        c.pop(-1)
    print(*c)
       