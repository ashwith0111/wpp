import random as r
lis = []
for i in range(1,101):
    lis.append(r.randint(0, 1))
s=0
a=0
for i in lis:
    if(i==0):
        s+=1
    else:
        if(s>a):
            a = s
        s = 0
if(s>a):
    a = s
print(lis)
print(a)