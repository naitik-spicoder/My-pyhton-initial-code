import random
while True:
    choic=["rock","paper","scissor"]
    user=input("what you want to choose(rock,paper,scissor) = ")
    comp=random.choice(choic)
    if user==comp:
        print("computer choose",user,"\nmatch tie")
    elif (user=="scissor") and (comp=="paper"):
        print("computer choose paper\nyou win")
    elif user=="paper" and comp=="scissor":
        print("computer choose scissor\ncomputer win,you lose")     
    elif user=="rock" and comp=="paper":
        print("computer choose paper\nyou lose")
    elif user=="paper" and comp=="rock":
        print("computer choose rock\nyou win")    
    elif user=="rock" and comp=="scissor":
        print("computer choose scissor\nyou win")     
    elif user=="scissor" and comp=="rock":
        print("computer choose rock\nyou lose") 