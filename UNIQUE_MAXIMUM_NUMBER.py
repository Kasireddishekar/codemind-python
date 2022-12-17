n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    b=a.count(i)
    if b==1 and i>s:
        s=i
if s>0:
    print(s)
else:
    print(-1)