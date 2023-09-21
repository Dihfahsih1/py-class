# Define a list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to list tasks
def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index. Please enter a valid task number.")

# Function to update a task
def update_task(task_index, updated_task):
    if 1 <= task_index <= len(tasks):
        old_task = tasks[task_index - 1]
        tasks[task_index - 1] = updated_task
        print(f"Task '{old_task}' updated to '{updated_task}' successfully!")
    else:
        print("Invalid task index. Please enter a valid task number.")

# Main loop
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to update: "))
        updated_task = input("Enter the updated task: ")
        update_task(task_index, updated_task)
    elif choice == "4":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
