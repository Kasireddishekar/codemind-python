n=int(input())
s=0
while n>0:
    rem=n%10
    n=n//10
    if rem>s:
        s=rem
print(s)