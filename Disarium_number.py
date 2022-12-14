n=int(input())
temp=n
c=0
s=0
su=0
while n>0:
    c=c+1
    r=n%10
    s=s*10+r
    n=n//10
i=1
while s>0 and i<=c:
    re=s%10
    su=su+pow(re,i)
    i+=1
    s=s//10
if temp==su:
    print("True")
else:
    print("False")
        
        
        
    
