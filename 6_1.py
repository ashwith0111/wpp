class pm:
    lis = []
    def set_pass(self,pas):
        if pas not in self.lis:
            self.lis.append(pas)
            print("Password Updated")
        else:
            print("This password already exists")
    def get_pass(self):
        if self.lis:
            print(f"The current password is {self.lis[-1]}")
        else:
            print("You have to give a password to get")
    def check(self,pas):
        if pas ==  self.lis[-1]:
            print("Given string is your password")
        else:
            print("Given string is not your password")
user = pm()
while True:
    print("1.To set a password\n2.")
    ca = int(input("Give the case number"))
    match ca:
        case 1:
            st = input("Give a new password")
            user.set_pass(st)
        case 2:
            user.get_pass()
        case 3:
            st = input("Type the cuurent password")
            user.check(st)
        case 4:
            print("THANK YOU")
            break
        case _:
            print("INVALID CHOICE")