from random import randint
def guss(x):
    random_number=randint(1,x)
    gusse=0
    while gusse != random_number:
        gusse=int(input(f"Enter the number between 1 and {x}: "))
        if gusse>random_number:
            print("it's to high,try again")
        elif gusse<random_number:
            print("it's too low,try again")
    print(f"hurray!you win the game the correct no is {random_number}")
guss(100)                
