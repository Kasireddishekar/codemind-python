l=int(input())#1
r=int(input())#3
c=0
s=0
for i in range(l,r+1):#(1,4)
    for j in range(i,r+1):#(1,4)
        for k in range(i,j+1):
            s=s+k
        if s%2==1:
            c=c+1
        s=0
print(c)
           
        
            
    