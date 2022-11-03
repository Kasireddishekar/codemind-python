import math
n=int(input())
root=int(math.sqrt(n))
if root**2==n:
    print("True")
else:
    print("False")