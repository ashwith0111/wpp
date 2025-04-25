import random as r
class rpc:
    cw,pw,nr=0,0,0
    def __init__(self,total):
        self.total = total
    def win(self,pm):
        choice = r.choice(['rock','paper','scissors'])
        self.nr +=1
        if choice == pm:
            print(f"Tie for the {self.nr} round")
        elif choice == 'rock' and pm == 'paper' or\
        choice == 'paper' and pm == 'scissors' or\
        choice == 'scissors' and pm == 'rock':
            self.pw+=1
            print(f"Player won the {self.nr} round")
        else:
            print(f"Computer won the {self.nr} round")
            self.cw+=1
    def fw(self):
        if self.cw>self.pw:
            print(f"Computer won the game")
        elif self.pw>self.cw:
            print(f"Player won the game")
        else:
            print("Tie")
nr = int(input("Give the number of rounds to be played: "))
game = rpc(nr)
i=0
while i<nr:
    pc = input("Give the player move: ")
    pc = pc.lower()
    if pc in ['rock','paper','scissors']:
        game.win(pc)
        i+=1
    else:
        print("Give a playable move")
game.fw()
print(f"scores are: \nPlayer->{game.pw}\nComputer->{game.cw}")