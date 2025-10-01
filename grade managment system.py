def grade():
	data={}
	print("GRADE MANAGMENT SYSTEM")
	while True:
	     menu=input("enter\n1 for add\n2 for update marks of student\n3 for remove/delete student\n4 for view\n5 for stop/exit\n-> ")
	     if menu.isdigit():
         	menu=int(menu)
         	if menu==3:
         		name_std=input("enter the name of student you want to remove-> ")
         		del data[name_std]
         		print(name_std,"removed")
         	elif menu==4:
         		for name,grade in data.items():
         			print(f"{name}:{grade}")
         	elif menu==5:
         		break			
         	elif menu==1:
         		new_std=input("enter the name of new student-> ")
         		new_mrk=input("enter the marks of student-> ")
         		data.update({new_std:new_mrk})
         		print("The marks of student",new_std,"is added")
         	elif menu==2:
         	    name=input("enter the name of student-> ")
         	    mrk=int(input("Enter new marks of student-> "))
         	    data[name]=mrk
         	    print(name,"marks has been updated")
         	      			
grade()	     
		