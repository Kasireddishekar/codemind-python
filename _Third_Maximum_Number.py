n=int(input())
a=list(map(int,input().split()))
b=set(a)
l=len(b)
c=0
if l>=3:
    while c<=2:
        m=max(b)
        b.remove(m)
        c+=1
    print(m)
else:
    print(max(b))
    
