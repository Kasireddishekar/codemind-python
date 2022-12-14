s=input()#12
a=int(s)**2#144
s1=s[::-1]#21
b=int(s1)**2#441
c=str(b)
d=c[::-1]#441
e=int(d)
if e==a:
    print("True")
else:
    print("False")