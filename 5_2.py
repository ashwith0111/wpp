ca = int(input("No of cases: "))
list=[]
for i in range(ca):
    n = int(input("Give the number: "))
    if n%2==1:
        list.append((n//2)*(n//2+1))
    else:
        list.append((n//2)**2)
for i in list:
    print(i)