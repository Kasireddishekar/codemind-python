a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    k=0
    c=0
    x=0
    if i==a-1:
        print(k)
    else:
        for j in range(i+1,a):
            k=k+1
            if b[i]<b[j] and c==0:
                c=c+1
                if c==1:
                    print(k,end=" ")
                else:
                    print(x,end=" ")
                break
        else:
            print(x,end=" ")
            
                    
              
   
    
    
    