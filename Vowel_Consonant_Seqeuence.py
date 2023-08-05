a=input()
b='aeiou'
c=0
d=0
for i in a:
    if i in b and c==0:
        print("V",end="")
        c=1
        d=0
    elif i not in b and d==0:
        print("C",end="")
        c=0
        d=1
        