n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in a:
    if i%2==1:
        c=c+1
        m=c
        if m>s:
            s=m
    elif i%2==0:
        c=0
print(s)