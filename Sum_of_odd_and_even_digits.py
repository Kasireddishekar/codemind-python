n=int(input())
a=list(map(int,input().split()))
s=0
su=0
for i in range(n):
    if i%2==0:
        s=s+a[i]
    else:
        su=su+a[i]
if su-s==0:
    print("YES")
else:
    print("NO")