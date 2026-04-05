# Mini Project #5: File-Based To Do List
# Features: add/view/delete tasks saved in a text file (persists after restart)

FILE_NAME = "to_do.txt"


def load_tasks():
    """Return a list of tasks (strings) from the file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f if line.strip()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Overtime the file with the provided tasks list."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\n No Tasks yet.\n")
        return
    
    print("\n Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    new_task = input("\nType your new task: ").strip()
    if not new_task:
        print(" Task can't be empty.\n")
        return

    tasks.append(new_task)
    save_tasks(tasks)
    print(" Task added!\n")

def delete_task(tasks):
    if not tasks:
        print("\n No tasks to delete.\n")
        return
   
    view_tasks(tasks)
    choice = input("Enter the task number to delete: ").strip()

    if not choice.isdigit():
        print(" Please enter a valid number.\n")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print(" That number isn't in the list.\n")
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f" Deleted: {removed}\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("==== TO-DO LIST ====")
        print("1) View tasks")
        print("2) Add task")
        print("3) Delete task")
        print("4) Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\n Saved. See you next time!\n")
            break
        else:
            print("\n Please choose 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
       
