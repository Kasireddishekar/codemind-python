a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=len(a)
A=0
B=0
for i in range(0,n):
    if a[i]>b[i]:
        A=A+1
    elif a[i]<b[i]:
        B=B+1
print(A,B)

        
        
    