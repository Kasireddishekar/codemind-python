a=list(map(int,input().split(',')))
c=0
for i in set(a):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s=s+j
    for k in set(a):
        if s==k:
            print(i,end=" ")
            c=1
if c==0:
    print(-1)
            