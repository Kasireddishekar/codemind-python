n=int(input())
a=list(map(int,input().split()))
b=set(a)
s=0
for i in b:
    c=a.count(i)
    if c>s:
        s=c
        e=i
print(e)