n=int(input())
a=0
b=1
d=[0,1]
for i in range(n):
    c=a+b
    d.append(c)
    a=b
    b=c
if n in d:
    print("True")
else:
    print("False")
    
    
    