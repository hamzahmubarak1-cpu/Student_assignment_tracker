task = []
completedTask = []
Incompleted_tasks = []
new_id = 1
Level = ["high","medium","low"]
def ad1d_task():
    '''This function basically takes the following values and adds to a dictionary, and from there I basically used 
    while loops for validation, This part is complete and fully works as inteded. '''
    global new_id
    add_Task = input("Enter your task: ")
    Course = input("Enter course: ")
    Due_date = input("Enter due date in Format (MM/DD/YYYY): ")
    Priority = input("Enter priority Level (High, Medium, Low): ")
    while Priority.lower() not in ["high", "medium", "low"]:
        Priority = input("Invalid priority. Enter again: ")
    while add_Task.strip() == "":
        add_Task = input("Invalid task. Enter your task again: ")
    while Course.strip() == "":
        Course = input("Invalid Course. Enter your Course again: ")
    while Due_date.strip() == "":
        Due_date = input("Invalid Date. Enter in (MM/DD/YYYY): ")
    To_Do = {
    
        "id": new_id,
        "Task":  add_Task,
        "course": Course,
        "Due Date": Due_date,
        "Priority": Priority,
        "Completed": False
        
    }
    task.append(To_Do)
    Incompleted_tasks.append(To_Do)
    print("Task added!")
    new_id+=1
def completeTask():
    '''In this complete task part, it marks the one to be completed, The main problem is when you try to get rid of the
    task because it will not let you. Ill try to fix this up later on'''
    print(task)
    com_task = int(input("The tasks you have are given above, would you like to mark one off? (1: yes, 0:no): "))
    if com_task == 1:
        choose = int(input("Choose the task (1-9999999)to complete:"))
        task[choose-1]['Completed'] = True
def view_Task():
    #for next time
    pass
def main():
    '''This is the main menu where the user whill choose his options, we still need to add a couple more like Recommend Task, View Points,Reward Point System to the main
    menu. '''
    flag = True

    while flag:
        print("===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Show Incomplete Tasks")
        print("6. Exit")

        action = int(input("Choose an action: "))
        if action == 6:
            flag = False
        elif (action == 1):
            ad1d_task()
        elif (action == 4):
            print(task)
        elif (action == 3):
            completeTask()

main()

