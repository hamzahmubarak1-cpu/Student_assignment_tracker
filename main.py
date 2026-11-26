task = []
completedTask = []
Incompleted_tasks = []
new_id = 1
Level = ["high","medium","low"]
point_counter = 0
def ad1d_task():
    '''This function basically takes the following values and adds to a dictionary, and from there I basically used 
    while loops for validation, This part is complete and fully works as inteded. '''
    global new_id
    add_Task = input("Enter your task: ")
    Course = input("Enter course: ")
    Due_dateM = int(input("Enter Month (MM): "))
    Due_dateD = int(input("Enter Day (DD): "))
    Due_dateY = int(input("Enter Year (YYYY): "))
    Priority = input("Enter priority Level (High, Medium, Low): ")

    while Priority.lower() not in ["high", "medium", "low"]:
        Priority = input("Invalid priority. Enter again: ")

    while add_Task.strip() == "":
        add_Task = input("Invalid task. Enter your task again: ")

    while Course.strip() == "":
        Course = input("Invalid Course. Enter your Course again: ")

    while Due_dateM < 1 or Due_dateM > 12:
        Due_dateM = int(input("Invalid month. Enter again: "))

    while Due_dateD < 1 or Due_dateD > 31:
        Due_dateD = int(input("Invalid day. Enter again: "))

    while Due_dateY < 2026 or Due_dateY > 2100:
        Due_dateY = int(input("Invalid year. Enter again: "))

    Due_date = f"{Due_dateM:02d}/{Due_dateD:02d}/{Due_dateY}"
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
    global point_counter
    '''Completing task function where it basically gives the tasks at hand and basically you mark one off by typing the id
    What works is setting the completion to True, and adding to the points, and also getting rid of the assignment. 
    
     WHAT NEEDS TO BE FIXED:
     So when you do remove it the id still gets stored as it came in from which we are going to have to fix. Once that is done this function should be complete
      
        '''
    print(task)
    com_task = int(input("The tasks you have are given above, would you like to mark one off? (1: yes, 0:no): "))
    if com_task == 1:
        choose = int(input("Choose the task (1-9999999)to complete:"))
        task[choose-1]['Completed'] = True
        point_counter +=1

    task.pop(choose-1)

def view_Task():
    '''This is not done because we need to sort based on priority level so High comes first Medium second then low last.'''
    print(task)
def viewPoints():
    '''View points just takes the amount of points the user has accumulated'''
    print(f"currently you have {point_counter} point/points")
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
        print("6. Edit Task")
        print("7. Recommend Task")
        print("8. View Points")
        print("9. Exit")

        action = int(input("Choose an action: "))
        if action == 9:
            flag = False
        elif (action == 1):
            ad1d_task()
        elif (action == 4):
            view_Task()
        elif (action == 3):
            completeTask()
        elif (action == 8):
            viewPoints()

main()

