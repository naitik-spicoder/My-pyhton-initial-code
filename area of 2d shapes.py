pi=22/7
print("2D shape:")
print("rectangle\nsquare\ncircle")
dim=int(input("enter the dimension(2 if 2D) = "))
if dim==2:
    shape=input("enter the shape = ")
    if shape=="rectangle":
        leng=int(input("enter the length of rectangle= "))
        breth=int(input("enter the width of rectangle = "))
        print("area of rectangle",leng*breth)
    elif shape=="square":
        side=int(input("enter the side of square= "))
        print("area of square is",side**2)
    elif shape=="circle":
       radius=int(input("enter the radius of the circle = "))    
       print("area of the circle is",pi*radius**2)