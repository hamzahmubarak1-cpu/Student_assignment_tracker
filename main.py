task = []
def ad1d_task():
    # num = 0
    add_Task = input("Enter your task: ")
    # counter=0
    To_Do = {
    
        "id": len(task)+1,
        "Task": add_Task,
        "Completed": "False"
    }
    task.append(To_Do)
    print("Task added!")
def main():
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

main()

