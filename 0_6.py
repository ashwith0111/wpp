a=int(input("give the first number: "))
rev=0
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
   