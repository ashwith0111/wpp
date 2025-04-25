class bank:
    ba = 0
    def __init__(self,name,id,bal):
        self.name = name
        self.bal = bal
        self.ba += bal
        self.id = id
    def deposit(self,bal):
        if bal<=0:
            print("INVALID AMOUNT")
        else:
            self.ba += bal
        print(f"the current balance is {self.ba}")
    def withdraw(self,bal):
        if self.ba<bal:
            print("NOT ENOUGH MONEY")
        elif bal<=0:
            print("INVALID AMOUNT")
        else:
            self.ba-=bal
            print(f"the current balance is {self.ba}")
    def display(self):
        print(f"name:{self.name}\nbalance:{self.ba}\naccount no:{id}")
name = input("Give the name: ")
while not name.isalpha():
    print("Give a valid name")
    name = input("Give the name: ")
bal = int(input("Give the amount you starting the account: "))
while bal<0:
    print("INVALID BALANCE")
    bal = int(input("Give the amount you starting the account: "))
id = int(input("account no: "))
a1 = bank(name,id,bal)
while True:
    ca = int(input("Give the case number: "))
    match ca:
        case 1:
            bal = int(input("Give the amount: "))
            a1.deposit(bal)
        case 2:
            bal = int(input("Give the: "))
            a1.withdraw(bal)
        case 3:
            a1.display()
        case 4:
            print("THANK YOU")
            break
        case _:
            print("INVALID")