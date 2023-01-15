a=int(input())
b=list(map(int,input().split()))
s=0
e=[]
for i in range(a):
    s=s*10+b[i]
k=s+1
while k:
    r=k%10
    e.append(r)
    k=k//10
e.reverse()
print(*e)
    

