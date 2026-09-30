# ==========================================
#           TO-DO LIST APPLICATION
#           First Semester Project
# ==========================================

tasks = []

while True:

    print("\n================================")
    print("          TO-DO LIST")
    print("================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":

        task = input("Enter your task: ")

        tasks.append({
            "task": task,
            "completed": False
        })

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\n--------- YOUR TASKS ---------")

            for i in range(len(tasks)):

                if tasks[i]["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(i + 1, ".", tasks[i]["task"], "-", status)

    # Mark Task as Completed
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\n--------- YOUR TASKS ---------")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])

            number = int(input("Enter task number to mark as completed: "))

            if number >= 1 and number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")

            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\n--------- YOUR TASKS ---------")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])

            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):
                deleted_task = tasks.pop(number - 1)
                print("Deleted:", deleted_task["task"])

            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":

        print("Thank you for using the To-Do List!")
        break

    # Wrong Choice
    else:

        print("Invalid choice. Please try again.")
