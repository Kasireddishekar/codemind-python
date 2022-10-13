a,b=map(int,input().split())
num=max(a,b)
num1=min(a,b)
if num==10 and num1==1:
    num=2
if num-num1==1:
        print("Yes")
else:
        print("No")
