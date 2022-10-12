num=int(input())
sum=0
pro=1
temp=num
while num>0:
    rem=num%10
    sum=sum+rem
    pro=pro*rem
    num=num//10
if sum==pro:
    print("Spy Number")
else:
    print("Not Spy Number")
    
    