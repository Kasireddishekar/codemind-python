n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    b=a[i]
    c=0
    for j in range(n):
        if a[j]<b:
            c=c+1
    print(c,end=" ")