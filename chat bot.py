from random import choice
from time import sleep


print("Hello! My name is robota 🤖")
sleep(1)
list=["Modern 😎","Traditional 🙇"]
comp=choice(list)
user_name=input("what is your name -> ")
sleep(1)
print(user_name,"is good name and it's a",comp,"name")
sleep(0.75)
change=input("you want to change my name y/n -> ")
if change=="y":
    new=input("enter my new name -> ")
    print("now my name is",new,"\nthanks for give me a new name")
if change=="n":
    print("thanks for respond ")
sleep(.75)      
age=int(input("what is your age -> "))
sleep(0.75)
if age<=18:
    print("oh! you are a young boy 🧒🧒")
if age>=18:
    print("omg! you are adult 🧑🧑🧑")   
if age>=40:
    print("oh! hello uncle ji 🧔")      
skill=input("what is your skills-> ")
sleep(0.5)   
print("I also like",skill) 
live=input("where do you live/abide-> ")
sleep(.75)
print("oh! I also visited here because I have Google map 😂😂😅")
sleep(1)
print("I think now you want to go and do your homework ")    
    