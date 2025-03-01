import os
import datetime

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found! Add a new task.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Add a task with priority and due date
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        priority = input("Set priority (Low, Medium, High): ").strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            priority = "Medium"  # Default priority
        due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        try:
            if due_date:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")  # Validate date
            else:
                due_date = "No due date"
        except ValueError:
            print("Invalid date format! Setting default due date.")
            due_date = "No due date"
        tasks.append(f"{task} [Priority: {priority}] [Due: {due_date}]")
        save_tasks(tasks)
        print("Task added!")

# Mark task as done
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] = f"[DONE] {tasks[task_num]}"
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Sort tasks by priority and due date
def sort_tasks(tasks):
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    tasks.sort(key=lambda x: (priority_order.get(x.split("[Priority: ")[-1].split("]")[0], 1), x.split("[Due: ")[-1].strip("]")))
    save_tasks(tasks)
    print("Tasks sorted by priority and due date!")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\nOptions: (1) View (2) Add (3) Complete (4) Remove (5) Sort by Priority & Due Date (6) Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose a number between 1-6.")

if __name__ == "__main__":
    main()
