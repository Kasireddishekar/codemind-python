n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=0
co=0
for i in b:
    c=a.count(i)
    if c>1:
        co=co+c//2
    c=0
print(co)