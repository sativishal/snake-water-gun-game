import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=='w':
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=='g':
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=='s':
            return False
        elif you=="w":
            return True

print("comp turn: snake(s) water(w) gun(g)  ")
rand_no= random.randint(1 , 3)
if rand_no==1:
    comp='s'
elif rand_no==2:
    comp='w'
elif rand_no==3:
    comp='g'

you=input("your turn: snake(s) water(w) gun(g)")
a=gamewin(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if a==None:
    print("this game is tied")
elif a:
    print("you win")
else:
    print("you lossed")