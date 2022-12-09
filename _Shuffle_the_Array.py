n=int(input())
a=list(map(int,input().split()))
for i in range(n//2):
    print(a[i],a[n//2+i],end=" ")
    