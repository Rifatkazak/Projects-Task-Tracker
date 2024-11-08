# Command-Line Task Manager

[Project Page: Projects-Task-Tracker](https://github.com/Rifatkazak/Projects-Task-Tracker)

This is a simple command-line task management application designed to help users track tasks through a JSON file. It allows users to add, update, delete, and mark tasks as in progress or done. This tool is suitable for quick task management directly from the terminal.

Features
Add, Update, and Delete Tasks: Create new tasks, modify existing tasks, or delete tasks as needed.
Status Tracking: Mark tasks as "in progress," "done," or "not done."
Listing Options: View all tasks or filter tasks by their status ("done," "not done," or "in progress").
Persistent Storage: Task data is stored in a JSON file located in the current directory.
Requirements
The application is designed to run from the command line.
The user provides inputs and actions as positional arguments.
All tasks are saved in a JSON file within the current directory.
The JSON file is created if it doesn’t already exist.
No external libraries or frameworks are required; only native file system operations are used.
Usage
Basic Commands
Add a Task

bash
Kodu kopyala
task_manager.py add "Task Title" "Task Description"
Adds a new task with a title and optional description.
Update a Task

bash
Kodu kopyala
task_manager.py update <task_id> "Updated Title" "Updated Description"
Updates the title and/or description of an existing task identified by <task_id>.
Delete a Task

bash
Kodu kopyala
task_manager.py delete <task_id>
Deletes the task with the specified <task_id>.
Mark Task as In Progress

bash
Kodu kopyala
task_manager.py mark_in_progress <task_id>
Marks the task with the specified <task_id> as "in progress."
Mark Task as Done

bash
Kodu kopyala
task_manager.py mark_done <task_id>
Marks the task with the specified <task_id> as "done."
Listing Tasks
List All Tasks

bash
Kodu kopyala
task_manager.py list
Lists all tasks.
List All Completed Tasks

bash
Kodu kopyala
task_manager.py list_done
Lists tasks marked as "done."
List All Incomplete Tasks

bash
Kodu kopyala
task_manager.py list_not_done
Lists tasks that are not marked as "done."
List All Tasks In Progress

bash
Kodu kopyala
task_manager.py list_in_progress
Lists tasks marked as "in progress."
Error Handling and Edge Cases
If the JSON file does not exist, the application will create it automatically.
The program validates inputs to ensure that actions are performed on valid task IDs.
Helpful error messages guide the user if any command or input is invalid.
Task lists are empty initially, and the application handles this gracefully by notifying the user when there are no tasks to display.
File Structure
task_manager.py: Main script handling user inputs and file operations.
tasks.json: JSON file where all task data is stored (created automatically if it doesn't exist).
Examples
bash
Kodu kopyala
# Adding a new task
python task_manager.py add "Buy Groceries" "Milk, eggs, bread"

# Marking a task as done
python task_manager.py mark_done 1

# Listing all tasks
python task_manager.py list

# Deleting a task
python task_manager.py delete 2
Notes
The JSON file is stored in the current directory, making it easy to back up or move task data.
The application relies solely on native file handling, ensuring lightweight, dependency-free operation.

