def lug(m):
    if m<=T:
       return 1
    else:
        return 2
N=int(input())
a=[]
for k in range(0,N):
    b=int(input())
    a.append(b)
T=int(input())
s=0
for i in a:
    s=s+lug(i)
print(s)
        
