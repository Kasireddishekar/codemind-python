n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
n3=int(input())
c=0
for i in range(n1):
    for j in range(a[i],b[i]+1):
        if j==n3:
            c=c+1
print(c)