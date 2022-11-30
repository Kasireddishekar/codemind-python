N=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    if i%2==0:
        c=c+1
    else:
        s=s+1
print(c,s)
