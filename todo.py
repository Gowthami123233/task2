import os


TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the tasks file. Returns a list of task strings."""
    if not os.path.exists(TASKS_FILE):
        return []
    tasks = []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task = line.rstrip("\n")
                if task:
                    tasks.append(task)
    except OSError as error:
        print(f"Error reading {TASKS_FILE}: {error}")
    return tasks


def save_tasks(tasks):
    """Persist tasks to the tasks file."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")
    except OSError as error:
        print(f"Error writing {TASKS_FILE}: {error}")


def print_menu():
    print("\n=== To-Do List ===")
    print("1) View tasks")
    print("2) Add task")
    print("3) Remove task")
    print("4) Exit")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    tasks.append(description)
    save_tasks(tasks)
    print("Task added.")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    list_tasks(tasks)
    choice = input("Enter the number of the task to remove: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Removed: {removed}")


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        selection = input("Choose an option (1-4): ").strip()

        if selection == "1":
            list_tasks(tasks)
        elif selection == "2":
            add_task(tasks)
        elif selection == "3":
            remove_task(tasks)
        elif selection == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
