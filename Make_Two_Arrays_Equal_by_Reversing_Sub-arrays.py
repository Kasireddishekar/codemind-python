n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
for i in a:
    if i not in b:
        print("False")
        break
else:
    print("True")