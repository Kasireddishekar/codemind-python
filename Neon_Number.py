num=int(input())
sum=0
s=num*num
while s>0:
    rem=s%10
    sum=sum+rem
    s=s//10
if num==sum:
    print("Neon Number")
else:
    print("Not Neon Number")