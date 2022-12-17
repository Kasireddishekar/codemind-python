a=int(input())
b=list(map(int,input().split()))
d=0
for i in b:
    c=0
    while i>0:
        c=c+1
        i=i//10
    if c%2==0:
        d=d+1
print(d)
