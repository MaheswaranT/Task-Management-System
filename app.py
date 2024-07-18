import os

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {self.description} - Due: {self.due_date} - Priority: {self.priority} - Status: {status}"

# Load tasks from file
def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                title, description, due_date, priority, completed = line.strip().split("|")
                task = Task(title, description, due_date, priority)
                task.completed = completed == "True"
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task.title}|{task.description}|{task.due_date}|{task.priority}|{task.completed}\n")

# Add a new task
def add_task(tasks):
    print("\nAdd Task")
    print("-" * 30)
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low/Medium/High): ")
    task = Task(title, description, due_date, priority)
    tasks.append(task)
    print("Task added successfully.")

# View tasks
def view_tasks(tasks):
    print("\nView Tasks")
    print("-" * 30)
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    print("\nUpdate Task")
    print("-" * 30)
    task_id = int(input("Enter task ID to update: ")) - 1
    if 0 <= task_id < len(tasks):
        task = tasks[task_id]
        print(f"Current title: {task.title}")
        title = input("Enter new title (leave blank to keep current): ")
        if title:
            task.title = title

        print(f"Current description: {task.description}")
        description = input("Enter new description (leave blank to keep current): ")
        if description:
            task.description = description

        print(f"Current due date: {task.due_date}")
        due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")
        if due_date:
            task.due_date = due_date

        print(f"Current priority: {task.priority}")
        priority = input("Enter new priority (Low/Medium/High, leave blank to keep current): ")
        if priority:
            task.priority = priority

        print("Task updated successfully.")
    else:
        print("Invalid task ID.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    print("\nDelete Task")
    print("-" * 30)
    task_id = int(input("Enter task ID to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        print("Task deleted successfully.")
    else:
        print("Invalid task ID.")

# Mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    print("\nMark Task as Completed")
    print("-" * 30)
    task_id = int(input("Enter task ID to mark as completed: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id].completed = True
        print("Task marked as completed.")
    else:
        print("Invalid task ID.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    tasks = load_tasks()
    while True:
        clear_console()
        print("=" * 40)
        print(" Task Management System ".center(40, "="))
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        print("=" * 40)
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
            input("\nPress Enter to return to the main menu...")
        elif choice == '2':
            view_tasks(tasks)
            input("\nPress Enter to return to the main menu...")
        elif choice == '3':
            update_task(tasks)
            input("\nPress Enter to return to the main menu...")
        elif choice == '4':
            delete_task(tasks)
            input("\nPress Enter to return to the main menu...")
        elif choice == '5':
            mark_task_completed(tasks)
            input("\nPress Enter to return to the main menu...")
        elif choice == '6':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the main menu...")
