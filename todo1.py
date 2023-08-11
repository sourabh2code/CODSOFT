# Define a dictionary to store the tasks
tasks = {}

# Function to add a task
def add_task(task_name, task_description):
    tasks[task_name] = task_description
    print("Task added:", task_name)

# Function to delete a task
def delete_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print("Task deleted:", task_name)
    else:
        print("Task not found:", task_name)

# Function to update a task
def update_task(task_name, new_description):
    if task_name in tasks:
        tasks[task_name] = new_description
        print("Task updated:", task_name)
    else:
        print("Task not found:", task_name)

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task_name, task_description in tasks.items():
            print("- Task:", task_name)
            print("  Description:", task_description)

# Main loop
while True:
    print("-----------------To-Do List Program--------------")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        add_task(task_name, task_description)
    elif choice == "2":
        task_name = input("Enter task name to delete: ")
        delete_task(task_name)
    elif choice == "3":
        task_name = input("Enter task name to update: ")
        new_description = input("Enter new task description: ")
        update_task(task_name, new_description)
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice (1/2/3/4/5).")
