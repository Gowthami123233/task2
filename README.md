# Persistent CLI To-Do App (Python)

A lightweight command-line to-do manager that stores tasks in a plain text file using Python’s built-in `open()`.

## Requirements
- Python 3.8+

## Run
```bash
python todo.py
```

## Features
- View tasks in a numbered list
- Add a task (saved to `tasks.txt`)
- Remove a task by number
- Tasks persist across runs (stored one-per-line in `tasks.txt`)

## How it works
- On start, the app loads tasks from `tasks.txt` into a Python list.
- On add/remove, the list is saved back to `tasks.txt` (UTF‑8).

## Sample session
=== To-Do List ===
1) View tasks
2) Add task
3) Remove task
4) Exit
Choose an option (1-4): 2
Enter task description: Buy milk
Task added.
Choose an option (1-4): 1
Your tasks:
Buy milk
Choose an option (1-4): 3
Enter the number of the task to remove: 1
Removed: Buy milk
Choose an option (1-4): 4
Goodbye!
