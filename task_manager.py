import json
import os
from datetime import datetime

#JSON File where tasks will be stored
TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the tasks.json file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save tasks to the tasks.json file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description, due_date=None):
    """Add a new task."""
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "due_date": due_date,
        "status": "pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added!")


def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, Status: {task['status']}")


def edit_task(tasks, task_id, new_description=None, new_due_date=None):
    """Edit a task."""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    if new_description:
        task['description'] = new_description
    if new_due_date:
        task['due_date'] = new_due_date
    save_tasks(tasks)
    print(f"Task {task_id} updated!")


def delete_task(tasks, task_id):
    """Delete a task."""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task {task_id} deleted!")


def mark_completed(tasks, task_id):
    """Mark a task as completed."""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    task['status'] = 'completed'
    save_tasks(tasks)
    print(f"Task {task_id} marked as completed!")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
            add_task(tasks, description, due_date if due_date else None)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Enter task ID to edit: "))
            new_description = input("Enter new description (leave empty to keep): ")
            new_due_date = input("Enter new due date (YYYY-MM-DD) or press Enter to keep: ")
            edit_task(tasks, task_id, new_description, new_due_date if new_due_date else None)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(tasks, task_id)
        elif choice == "6":
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()