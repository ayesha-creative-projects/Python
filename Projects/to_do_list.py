# To-Do List

tasks = []  # List to store tasks

while True:
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
        
    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for index, t in enumerate(tasks, start=1):
                print(f"{index}. {t}")
        else:
            print("No tasks found.")
            
    elif choice == "3":
        if tasks:
            for index, t in enumerate(tasks, start=1):
                print(f"{index}. {t}")
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num-1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")
            
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
