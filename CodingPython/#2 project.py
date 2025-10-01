import random
def guess(x):
    low=1
    high=x
    i=True
    while i:
        random_no=random.randint(low,high)
        feedback=input(f"computer choose {random_no} if high enter 'H' if low enter 'L' if correct enter 'C': ").upper()
        if feedback=="L":
            low+=1
        elif feedback=="H":
            high-=1
        elif feedback=="C":
            print("computer choose number correctly") 
            i=False
        else:
            print("   ")
guess(100) 