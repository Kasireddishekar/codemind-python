x,y=map(int,input().split())
z=y*2
if x==0 and y%2==0:
    print("YES")
elif x==0 and y%2!=0:
    print("NO")
elif x%2==0 and y==0:
    print("YES")
elif x%2==0 and z%2==0:
    print("YES")
else:
    print("NO")
    