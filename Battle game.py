
from random import choice 
a=["punch","kick","combo","poision"]
b=["punch","kick","combo","TNT","BIG TNT"]
c=["wings","head attack","paper bomb"]
wtch=choice(a)
wthr=choice(b)
endr=choice(c)

print("~~~~~~~~1 VS 1 BATTLE~~~~~~~~\nLOBBY:")
user1=int(input("enter 1 for play\nenter 2 for setting\nenter 3 for exit\n"))
if user1==1:
    print("~~TUTORIAL~~\nfor punch enter 1(infinite times)\nfor kick enter 2(infinite times)\nfor combo enter 3(only 3 times)\nfor sharingan enter 4(only 2 times)")
    user2=input("if you understand the tutorial then enter 'start'\n")
    if user2=="start":
        print("~~~LEVEL 1~~~\nNARUTO(you) with 100HP VS witch with 50HP")
        i=1
        adam_hp=100
        witch_hp=50
        while adam_hp>0 and witch_hp>0:
            n="enter your move= "
            move1=int(input(n))
            if move1==1:
                witch_hp-=5
                print("you hit puch,now the witch hp is",witch_hp)
                print("now witch time")
                if wtch=="punch":
                    print("witch attack: punch")
                    adam_hp-=5
                    print("your hp is",adam_hp) 
                elif wtch=="kick":
                    print("witch attack: kick")
                    adam_hp-=10
                    print("your hp is",adam_hp)
                elif wtch=="combo":
                    print("witch attack: combo")
                    adam_hp-=25
                    print("your hp is",adam_hp)
                elif wtch=="poision":
                    print("witch attack: poision")   
                    adam_hp-=50
                    print("your hp is",adam_hp)
                    
            elif move1==2:
                witch_hp-=10
                print("you hit kick,now witch hp is",witch_hp)     
                print("now witch time")  
                if wtch=="punch":
                    print("witch attack: punch")
                    adam_hp-=5
                    print("your hp is",adam_hp) 
                elif wtch=="kick":
                    print("witch attack: kick")
                    adam_hp-=10
                    print("your hp is",adam_hp)
                elif wtch=="combo":
                    print("witch attack: combo")
                    adam_hp-=25
                    print("your hp is",adam_hp)
                elif wtch=="poision":
                    print("witch attack: poision")   
                    adam_hp-=50
                    print("your hp is",adam_hp)
            elif move1==3:
                witch_hp-=25
                print("you hit combo,now witch hp is",witch_hp)
                print("now witch time")
                if wtch=="punch":
                    print("witch attack: punch")
                    adam_hp-=5
                    print("your hp is",adam_hp) 
                elif wtch=="kick":
                    print("witch attack: kick")
                    adam_hp-=10
                    print("your hp is",adam_hp)
                elif wtch=="combo":
                    print("witch attack: combo")
                    adam_hp-=25
                    print("your hp is",adam_hp)
                elif wtch=="poision":
                    print("witch attack: poision")   
                    adam_hp-=50
                    print("your hp is",adam_hp) 
            elif move1==4:                   
               witch_hp-=50
               print("you hit sharingan,now witch hp is",witch_hp)   
               print("now witch time")
               if wtch=="punch":
                    print("witch attack: punch")
                    adam_hp-=5
                    print("your hp is",adam_hp) 
               elif wtch=="kick":
                    print("witch attack: kick")
                    adam_hp-=10
                    print("your hp is",adam_hp)
               elif wtch=="combo":
                    print("witch attack: combo")
                    adam_hp-=25
                    print("your hp is",adam_hp)
               elif wtch=="poision":
                    print("witch attack: poision")   
                    adam_hp-=50
                    print("your hp is",adam_hp)
        if adam_hp>witch_hp:
              print("-----------------------------")
              print("congratulations,YOU WIN")
              print("-----------------------------")     
        elif adam_hp<witch_hp:
              print("nice try,but you lose")                                            
        print("~~~LEVEL 2~~~\nNARUTO(you) with hp 100 VS WITHER with hp 100")
        adam2_hp=100
        wither_hp=100
        while adam2_hp>0 or wither_hp>0:
             move2=int(input(n))
             if move2==1:
                 wither_hp-=5
                 print("you hit:punch,Noe wither hp is",wither_hp)
                 print("now it's wither time")
                 if wthr=="punch":
                     adam2_hp-=5
                     print("wither hit:punch,now your hp is",adam2_hp)
                 elif wthr=="kick":
                     adam2_hp-=20
                     print("wither hit:kick,now your hp is",adam2_hp)
                 elif wthr=="combo":
                     adam2_hp-=25
                     print("wither hit:combo,now your hp is",adam2_hp)
                 elif wthr=="TNT":
                     adam2_hp-=50
                     print("wither hit:TNT,now your hp is",adam2_hp)
                 elif wthr=="BIG TNT":
                     adam2_hp-=75
                     print("wither hit:BIG TNT,now your hp is",adam2_hp)
             elif move2==2:
                 wither_hp-=10
                 print("you hit:kick,now wither hp is",wither_hp)
                 print("now it's wither time")   
                 if wthr=="punch":
                     adam2_hp-=5
                     print("wither hit:punch,now your hp is",adam2_hp)
                 elif wthr=="kick":
                     adam2_hp-=20
                     print("wither hit:kick,now your hp is",adam2_hp)
                 elif wthr=="combo":
                     adam2_hp-=25
                     print("wither hit:combo,now your hp is",adam2_hp)
                 elif wthr=="TNT":
                     adam2_hp-=50
                     print("wither hit:TNT,now your hp is",adam2_hp)
                 elif wthr=="BIG TNT":
                     adam2_hp-=75
                     print("wither hit:BIG TNT,now your hp is",adam2_hp)
             elif move2==3:
                 wither_hp-=25
                 print("you hit:combo,now wither hp is",wither_hp)
                 print("now it's wither time")   
                 if wthr=="punch":
                     adam2_hp-=5
                     print("wither hit:punch,now your hp is",adam2_hp)
                 elif wthr=="kick":
                     adam2_hp-=20
                     print("wither hit:kick,now your hp is",adam2_hp)
                 elif wthr=="combo":
                     adam2_hp-=25
                     print("wither hit:combo,now your hp is",adam2_hp)
                 elif wthr=="TNT":
                     adam2_hp-=50
                     print("wither hit:TNT,now your hp is",adam2_hp)
                 elif wthr=="BIG TNT":
                     adam2_hp-=75
                     print("wither hit:BIG TNT,now your hp is",adam2_hp)
             elif move2==4:
                 wither_hp-=50
                 print("you hit:sharingan,now wither hp is",wither_hp)
                 print("now it's wither time")   
                 if wthr=="punch":
                     adam2_hp-=5
                     print("wither hit:punch,now your hp is",adam2_hp)
                 elif wthr=="kick":
                     adam2_hp-=20
                     print("wither hit:kick,now your hp is",adam2_hp)
                 elif wthr=="combo":
                     adam2_hp-=25
                     print("wither hit:combo,now your hp is",adam2_hp)
                 elif wthr=="TNT":
                     adam2_hp-=50
                     print("wither hit:TNT,now your hp is",adam2_hp)
                 elif wthr=="BIG TNT":
                     adam2_hp-=75
                     print("wither hit:BIG TNT,now your hp is",adam2_hp)                                      
        if adam2_hp>wither_hp:
            print("-----------------------------")
            print("congratulations,YOU WIN and you kill the wither")
            print("-----------------------------")       
        elif adam2_hp<wither_hp:
            print("nice try,but you lose")
        else:
            print("match tie")    
        print("~~~LEVEL 3~~~\nNARUTO(you) with 100 hp VS ENDER DRAGON with 200 hp")
        adam3_hp=100
        ender_hp=200
        while adam3_hp>0 or ender_hp>0:
            move3=int(input(n))     
            if move3==1:
                ender_hp-=5
                print("you hit:punch,Now ender dragon hp is",ender_hp)
                print("now it's dragon time")
                if endr=="wings":
                    adam3_hp-=25
                    print("dragon hit:wings,now your hp is",adam3_hp)     
                elif endr=="head attack":
                    adam3_hp-=50
                    print("dragon hit:head attack,now your hp is",adam3_hp)
                elif endr=="paper bomb":
                    adam3_hp-=100
                    print("dragon hit:paper bomb,now your hp is",adam3_hp)                                                
            if move3==2:
                ender_hp-=10
                print("you hit:kick,Now ender dragon hp is",ender_hp)
                print("now it's dragon time")
                if endr=="wings":
                    adam3_hp-=25
                    print("dragon hit:wings,now your hp is",adam3_hp)     
                elif endr=="head attack":
                    adam3_hp-=50
                    print("dragon hit:head attack,now your hp is",adam3_hp)
                elif endr=="paper bomb":
                    adam3_hp-=100
                    print("dragon hit:paper bomb,now your hp is",adam3_hp)     
            if move3==3:
                ender_hp-=25
                print("you hit:combo,Now ender dragon hp is",ender_hp)
                print("now it's dragon time")
                if endr=="wings":
                    adam3_hp-=25
                    print("dragon hit:wings,now your hp is",adam3_hp)     
                elif endr=="head attack":
                    adam3_hp-=50
                    print("dragon hit:head attack,now your hp is",adam3_hp)
                elif endr=="paper bomb":
                    adam3_hp-=100
                    print("dragon hit:paper bomb,now your hp is",adam3_hp)   
            if move3==4:
                ender_hp-=50
                print("you hit:sharingan,Now ender dragon hp is",ender_hp)
                print("now it's dragon time")
                if endr=="wings":
                    adam3_hp-=25
                    print("dragon hit:wings,now your hp is",adam3_hp)     
                elif endr=="head attack":
                    adam3_hp-=50
                    print("dragon hit:head attack,now your hp is",adam3_hp)
                elif endr=="paper bomb":
                    adam3_hp-=100
                    print("dragon hit:paper bomb,now your hp is",adam3_hp)
        if adam3_hp>ender_hp:
            print("-----------------------------") 
            print("congratulations YOU WIN,now you win full game")
            print("-----------------------------") 
        elif adame_hp<ender_hp:
           print("nice try,but you lose")     
        else:
           print("match tie")                                                                                                                                                                                                                                                                
                                                                                      