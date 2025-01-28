string = input("Give a string: ")
j=0
for i in string:
    if j%2==0:
        i = i.lower()
    else:
        i = i.upper()
    j+=1
    print(i,end="")