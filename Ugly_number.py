n=int(input())
c=0
while n!=1:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//2
    elif n%5==0:
        n=n//2
    else:
        c=c+1
        break
if c==1:
    print("Not Ugly Number")
else:
    print("Ugly Number")