
# define the list which will contail the daily tasks
tasks_list=[]
# the enterance message which will be displayed for the user every time 
enterance_message="""
please choose an option to continue:
1 - add a new task
2- display your current list
3- complete a task
4- quit the app
"""

def main_app():
    #the main loop of tha App
    while True:
       print(enterance_message)
       choice=input("your choice (please enter the number of the desired task 1-4) :")

       if choice=='1':
          add_task()
    
       elif choice=='2':
          display_list()
    
       elif choice=='3':
          complete_task()
    
 
       elif choice =='4':
          print("thank you for using  the app!")
          break
       else:
          print("invalid input,please enter the right number (from 1 to 6) which represent the option you want ")

def add_task():
    #get the task from the user
    task=input("pleas enter the task name: ")
    #store the task name and its stats(completed or not) in a dictionary
    task_info={'task':task,'status':False}
    #add the task info into the tasks list
    tasks_list.append(task_info)
    print("task added to the tasks list successfuly")

def complete_task():
    #disply the list for the user to know which tasks are not completed
    display_list()
    # a flag to know if this task is found
    f=0
    # a loop to take the right input from the user
    
    while True:
        if len(tasks_list)==0:
            print("your task list is empty , sorry!")
            break
        elif all( item['status']  for item in tasks_list ):
            print("you completed all your tasks!")
            break

        task= input("please enter the name of task that you completed: ")
        for item in tasks_list:
            if task== item['task'] :
                item['status']=True

                f=1
                print("the task marked complete successfuly")

        if  f :
            break
       
        if not f:
            task=input("the task you entered can't be found,please enter it again")
                   
def display_list():
    if len(tasks_list)==0:
        print("your to-do-list is empty!")
        return
    print("your to-do-list :")
    for item in tasks_list:
        print(f"{item['task']}:","Completed" if item['status'] else "not Completed")
 
main_app()





