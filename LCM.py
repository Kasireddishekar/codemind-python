num1,num2=map(int,input().split())
num=max(num1,num2)
while True:
    if num%num1==0 and num%num2==0:
        print(num)
        break
    num=num+1


