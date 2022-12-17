n=int(input())
a=list(map(int,input().split()))
c=a.count(0)
for i in range(0,c):
    a.remove(0)
for i in range(0,c):
    a.append(0)
print(*a)