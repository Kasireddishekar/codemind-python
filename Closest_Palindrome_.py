n=int(input())
for i in range(n-1,10,-1):
    s=0
    temp=i
    while i>0:
        r=i%10
        s=s*10+r
        i=i//10
    if temp==s:
        d=n-s
        p1=s
        break
for j in range(n+1,2*n,1):
    s1=0
    temp1=j
    while j>0:
        r1=j%10
        s1=s1*10+r1
        j=j//10
    if temp1==s1:
        d1=s1-n
        p2=s1
        break
if d<d1:
    print(p1)
elif d==d1:
    print(p1,p2)
else:
    print(p2)
        