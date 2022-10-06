def sdn (num):
    temp=num
    while temp:
        d=temp%10
        temp=temp//10
        if d==0 or num%d!=0:
            return False
    return True
num1=int(input())
num2=int(input())
for i in range(num1,num2+1):
    if sdn(i):
        print(i,end=" ")