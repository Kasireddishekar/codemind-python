n=int(input())
a=list(map(int,input().split()))
d=int(input())
b=max(a)
for i in a:
    c=d+i
    if c>=b:
        print("True",end=" ")
    else:
        print("False",end=" ")