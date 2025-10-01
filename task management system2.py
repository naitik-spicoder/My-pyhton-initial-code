def task():
    tasks=[]
    print("-----task management app-----") 
    total_task=int(input("how many task you want to save = "))
    for i in range(1,total_task+1):
        task_name=input("enter task  = ")
        tasks.append(task_name)
    print("today task is\n",tasks)    
    while True:
        
        
        operation=input("enter:\n1 for add\n2 for update\n3 for delete\n4 for view\n5 for exit/stop\n=")
        
        if operation=="1":
            add=input("which task you want to add = ")
         
            tasks.append(add)
            print("your task has been added ")
        elif operation=="2":
               update=input("which task you want to update = ")
               if update in tasks:
                   idx=tasks.index(update)
                   tasks.remove(update)
                   new=input("enter your new task = ")
                   tasks.insert(idx,new)
                   print(update,"updated to",new)
                   
        elif operation=="3":
                   dlt=input("which value you want to delete= ")
                   if dlt in tasks:
                       tasks.remove(dlt)
                       print(dlt,"removed")
        elif operation=="4":
               print("today's tasks is",tasks)    
               
        elif operation=="5":
               break
        else:
               print("invalid operation" )           
               
task()                       