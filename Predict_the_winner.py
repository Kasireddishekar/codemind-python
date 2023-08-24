n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=0
e=0
for i in a:
    if d==0:
        b.append(i)
        d=1
        e=0
    elif e==0:
        c.append(i)
        d=0
        e=1
s=sum(b)
s1=sum(c)
s2=abs(s-s1)
if s2%4==0:
    print("X")
else:
    print("Y")
        
    