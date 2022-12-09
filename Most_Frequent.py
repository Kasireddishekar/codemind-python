N=int(input())
a=list(map(int,input().split()))
c={}
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1
m=0
for k in c:
    if c[k]>m:
        m=c[k]
        l=k
print(l)
   
