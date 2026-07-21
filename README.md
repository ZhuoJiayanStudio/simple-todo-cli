# simple-todo-cli

A tiny command-line to-do list app written in Python. Tasks are stored locally
in `tasks.json`, no external dependencies required.

## Requirements
- Python 3.8+

## Usage

```bash
# Add a task
python todo.py add "Buy groceries"

# List all tasks
python todo.py list

# Mark a task as done (by its number from `list`)
python todo.py done 1

# Remove a task (by its number from `list`)
python todo.py remove 1
```

## Contributing
Check the [Issues](../../issues) tab for open tasks labeled `good first issue`.
