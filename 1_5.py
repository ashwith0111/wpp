i=0
list1=[]
name = input("Give the name upto 15 letters: ")
while i<2:
    if len(name)>15:
        print("Give the name upto 15 characters")
        name = input("Give the name upto 15 letters: ")
    else:
        name = name[::-1]
        list1.append(name)
        i+=1
        name = input("Give the name upto 15 letters: ")
name = name[::-1]
list1.append(name)
print(list1)