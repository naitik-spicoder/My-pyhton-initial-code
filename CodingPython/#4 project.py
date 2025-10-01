import string
import random
words=["kite","king","pine","skin"]
word=random.choice(words)
w_list=[x for x in word]
blank="-"*len(word)
b_list=[i for i in blank]
print(b_list)
def hangman():
    lifes=7  
    print("~~~~~~~~WELCOME TO HANGMAN GAME~~~~~~~~")
    print("You have 7 lifes")
    while lifes>0:
        get_letter=input("\nguess a letter and find the word: ")
        if get_letter in w_list:
            idx=w_list.index(get_letter)
            b_list.pop(idx)
            b_list.insert(idx,get_letter)
            for i in b_list:
                print(i,end="")
                w="".join(b_list)                
            if w==word:
                print(f"\n~~~~~~~~CONGRATULATION YOU WIN~~~~~~~~\nthe correct word is {word}")
                break    
        else:
            print("wrong letter guess,try again")
            lifes-=1
            print(f"now you have {lifes} LIFES")
    if lifes==0:
        print("YOU LOSS,you waste your all lifes")                
#hangman()            