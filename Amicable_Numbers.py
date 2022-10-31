def pfs(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum
a=int(input())
b=int(input())
k=pfs(a)
l=pfs(b)
if k==b and l==a:
    print("Amicable")
else:
    print("Not Amicable")