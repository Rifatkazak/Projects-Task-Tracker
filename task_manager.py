import sys
import json
import os

# Constants
TASKS_FILE = "tasks.json"

# Helper functions
def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def find_task(task_id, tasks):
    """Find a task by ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def generate_task_id(tasks):
    """Generate a new unique task ID."""
    return max((task["id"] for task in tasks), default=0) + 1

# Commands
def add_task(title, description=""):
    """Add a new task."""
    tasks = load_tasks()
    task_id = generate_task_id(tasks)
    tasks.append({
        "id": task_id,
        "title": title,
        "description": description,
        "status": "not done"
    })
    save_tasks(tasks)
    print(f"Task '{title}' added with ID {task_id}.")

def update_task(task_id, title=None, description=None):
    """Update an existing task."""
    tasks = load_tasks()
    task = find_task(task_id, tasks)
    if task:
        if title:
            task["title"] = title
        if description:
            task["description"] = description
        save_tasks(tasks)
        print(f"Task ID {task_id} updated.")
    else:
        print(f"Task ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) < len(tasks):
        save_tasks(new_tasks)
        print(f"Task ID {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")

def mark_task(task_id, status):
    """Mark a task as done, in progress, or not done."""
    tasks = load_tasks()
    task = find_task(task_id, tasks)
    if task:
        task["status"] = status
        save_tasks(tasks)
        print(f"Task ID {task_id} marked as {status}.")
    else:
        print(f"Task ID {task_id} not found.")

def list_tasks(filter_status=None):
    """List tasks, optionally filtered by status."""
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if filter_status is None or task["status"] == filter_status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']} | Description: {task['description']}")
    else:
        print("No tasks found." if filter_status is None else f"No tasks with status '{filter_status}' found.")

# Command-line Interface
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command> [<args>...]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            title = sys.argv[2]
            description = sys.argv[3] if len(sys.argv) > 3 else ""
            add_task(title, description)

        elif command == "update":
            task_id = int(sys.argv[2])
            title = sys.argv[3] if len(sys.argv) > 3 else None
            description = sys.argv[4] if len(sys.argv) > 4 else None
            update_task(task_id, title, description)

        elif command == "delete":
            task_id = int(sys.argv[2])
            delete_task(task_id)

        elif command == "mark_in_progress":
            task_id = int(sys.argv[2])
            mark_task(task_id, "in progress")

        elif command == "mark_done":
            task_id = int(sys.argv[2])
            mark_task(task_id, "done")

        elif command == "mark_not_done":
            task_id = int(sys.argv[2])
            mark_task(task_id, "not done")

        elif command == "list":
            list_tasks()

        elif command == "list_done":
            list_tasks("done")

        elif command == "list_not_done":
            list_tasks("not done")

        elif command == "list_in_progress":
            list_tasks("in progress")

        else:
            print(f"Unknown command: {command}")
            print("Available commands: add, update, delete, mark_in_progress, mark_done, mark_not_done, list, list_done, list_not_done, list_in_progress")
    except IndexError:
        print("Error: Missing required arguments for the command.")
    except ValueError:
        print("Error: Invalid input. Task ID should be a number.")

if __name__ == "__main__":
    main()
