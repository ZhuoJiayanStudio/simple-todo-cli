"""
Simple Todo CLI
A basic command-line to-do list app that stores tasks in a local JSON file.

Usage:
    python todo.py add "Buy groceries"
    python todo.py list
    python todo.py done 1
    python todo.py remove 1
"""

import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    # NOTE: no validation yet on empty/whitespace-only descriptions.
    # See open issue: "Add input validation to the add command".
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added task: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python todo.py add \"Your task\"")
        return
    for i, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}. {task['description']}")


def complete_task(index):
    tasks = load_tasks()
    idx = index - 1
    if idx < 0 or idx >= len(tasks):
        print(f"No task numbered {index}.")
        return
    tasks[idx]["done"] = True
    save_tasks(tasks)
    print(f"Marked task {index} as done.")


def remove_task(index):
    tasks = load_tasks()
    idx = index - 1
    if idx < 0 or idx >= len(tasks):
        print(f"No task numbered {index}.")
        return
    removed = tasks.pop(idx)
    save_tasks(tasks)
    print(f"Removed task: {removed['description']}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) == 3:
        complete_task(int(sys.argv[2]))
    elif command == "remove" and len(sys.argv) == 3:
        remove_task(int(sys.argv[2]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
