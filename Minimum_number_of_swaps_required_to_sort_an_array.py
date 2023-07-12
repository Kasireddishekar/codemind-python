k=int(input())
a=list(map(int,input().split()))
c=0
for i in range(k):
    l=i
    d=0
    for j in range(i+1,k):
        if a[j]<a[l]:
            l=j
            d=1
    if d==1:
        a[i],a[l]=a[l],a[i]
        c+=1
print(c)
    
                
   
            
            
    
