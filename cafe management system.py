print("welcome to our cafe")
print("menu:")
print("coffee:50\nburger:40\ncream bun:45\nfries:80")
menu={

"coffee": 50,
"burger": 40,
"cream bun": 45,
"fries": 80,
}
ord=input("what's your order= ")    
print("your order is",ord,"and your order is confirmed")
intp=input("anything else you want to order= ")
if intp=="yes":
     ord2=input("what is your second order= ")
     print("your 2nd order is",ord2,"and your order is confirmed ")
     t="your total bill is"
     total=menu.get(ord)+menu.get(ord2)
     
     print(t,total)
else:
    print("your total bill is",menu.get(ord))     