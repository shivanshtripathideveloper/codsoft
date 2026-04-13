# To-Do List Application (CLI Based)

import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

# Add a task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("Task added successfully!\n")

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if tasks[num-1].startswith("[ ]"):
            tasks[num-1] = tasks[num-1].replace("[ ]", "[✔]")
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Task already completed!\n")
    except:
        print("Invalid input!\n")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted successfully!\n")
    except:
        print("Invalid input!\n")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")

if __name__ == "__main__":
    main()