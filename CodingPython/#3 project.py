import random
def r_p_c():
    c_list=["rock","paper","scissor"]
    comp_c=random.choice(c_list)
    user=input("Enter what you wan'a choose(rock,paper,scissor): ").lower()
    if user=="rock" and comp_c=="paper":
        print(f"Computer choose {comp_c}\nso,computer win and YOU LOSS")
    elif user=="rock" and comp_c=="scissor":
        print(f"Computer choose {comp_c}\n~~~~~~~~HURRAY YOU WIN~~~~~~~~")
    elif user=="paper" and comp_c=="rock":
        print(f"Computer choose {comp_c}\n~~~~~~~~HURRAY YOU WIN~~~~~~~~")
    elif user=="paper" and comp_c=="scissor":
        print(f"Computer choose {comp_c}\ncoputer win and YOU LOSS")
    elif user=="scissor" and comp_c=="rock":
        print(f"Computer choose {comp_c}\nComputer win and YOU LOSS")
    elif user=="scissor" and comp_c=="paper":
        print(f"Computer choose {comp_c}\n~~~~~~~~HURRAY YOU WIN~~~~~~~~")
    elif user==comp_c:
        print(f"MATCH WAS DIE,because computer and you both choose {comp_c}")
while True:
    r_p_c()                       