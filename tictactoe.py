def board(x,o):#making a board
    zero="X" if x[0] else ("O" if o[0] else 0)#conditional statment in variable
    one="X" if x[1] else ("O" if o[1] else 1)#eg 11 if 1 else
    two="X" if x[2] else ("O" if o[2] else 2)
    three="X" if x[3] else ("O" if o[3] else 3)
    four="X" if x[4] else ("O" if o[4] else 4)
    five="X" if x[5] else ("O" if o[5] else 5)
    six="X" if x[6] else ("O" if o[6] else 6)
    seven="X" if x[7] else ("O" if o[7] else 7)
    eight="X" if x[8] else ("O" if o[8] else 8)
    print(f"{zero}|{one}|{two}")
    print("-|-|-")
    print(f"{three}|{four}|{five}")
    print("-|-|-")
    print(f"{six}|{seven}|{eight}")
x=[0,0,0,0,0,0,0,0,0]
o=[0,0,0,0,0,0,0,0,0]
turn=1
board(x,o)
while True:
    if turn==1:
        print("'X' turn now")
        user=int(input("Enter the index with respect to board: "))
        if x[user]==1 or o[user]==1:
            print("this index also has a player")
        elif x[user]==0:
            x[user]=1    
            board(x,o)
        if x[0]==x[1]==x[2]==1 or x[3]==x[4]==x[5]==1 or x[6]==x[7]==x[8]==1:
            #checking horizontaly the o win or not
            print("~~~~~~~~HURRAY! X WIN THE GAME~~~~~~~~")
            break
        elif x[0]==x[3]==x[6]==1 or x[1]==x[4]==x[7]==1 or x[2]==x[5]==x[8]==1:
            #checking vertically o win or not
            print("~~~~~~~~HURRAY! X WIN THE GAME~~~~~~~~")
            break
        elif x[0]==x[4]==x[8]==1 or x[2]==x[4]==x[6]==1:
            #checking diogonaly o win or not
            print("~~~~~~~~HURRAY! X WIN THE GAME~~~~~~~~")
            break
        turn-=1    
    elif turn==0:
        print("'O' turn now")
        user=int(input("Enter the index with respect to board: "))
        if o[user]==1 or x[user]==1:
            print("this index have a player")
        elif o[user]==0:
            o[user]=1    
            board(x,o)
        if o[0]==o[1]==o[2]==1 or o[3]==o[4]==o[5]==1 or o[6]==o[7]==o[8]==1:
            #checking horizontaly the o win or not
            print("~~~~~~~~HURRAY! O WIN THE GAME~~~~~~~~")
            break
        elif o[0]==o[3]==o[6]==1 or o[1]==o[4]==o[7]==1 or o[2]==o[5]==o[8]==1:
            #checking vertically o win or not
            print("~~~~~~~~HURRAY! O WIN THE GAME~~~~~~~~")
            break
        elif o[0]==o[4]==o[8]==1 or o[2]==o[4]==o[6]==1:
            #checking diogonaly o win or not
            print("~~~~~~~~HURRAY! O WIN THE GAME~~~~~~~~")
            break
        turn+=1

        

        
