import json

def add_task(task_list):
    task_name = input("Enter the task name: ")
    task_list.append(task_name)
    print("Task added successfully.")
    
def delete_task(task_list):
    task_name = input("Enter the task name: ")
    if task_name in task_list:
        task_list.remove(task_name)
        print("Task deleted successfully.")
    else:
        print("Task not found in the list.")
    
def view_tasks(task_list):
    if task_list:
        print("Your current list of tasks:")
        for i, task in enumerate(task_list):
            print(str(i+1) + ". " + task)
    else:
        print("Your task list is currently empty.")

def save_tasks(task_list):
    with open("task_list.json", "w") as f:
        json.dump(task_list, f)
    print("Task list saved to file.")

def load_tasks():
    try:
        with open("task_list.json", "r") as f:
            task_list = json.load(f)
        print("Task list loaded from file.")
    except FileNotFoundError:
        task_list = []
        print("Task list file not found. Starting with an empty list.")
    return task_list

def main():
    task_list = load_tasks()
    
    while True:
        print("Menu:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. Save tasks to file")
        print("5. Load tasks from file")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            delete_task(task_list)
        elif choice == "3":
            view_tasks(task_list)
        elif choice == "4":
            save_tasks(task_list)
        elif choice == "5":
            task_list = load_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
