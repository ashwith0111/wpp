dict1 = {}
pn = input("Give the product name: ")
pr = int(input("Give the product price: "))
while(pn != "STOP"):
    dict1[pn] = pr
    pn = input("Give the product name: ")
    pr = int(input("Give the product price: "))
search = input("Give the product name to search: ")
while(search != "STOP"):
    if search in dict1:
        print(f"the price of the product is {dict1[search]}")
    else:
        print("Give string is not present in the product name's")
    search = input("Give the product name to search: ")
print("Thank you")
    