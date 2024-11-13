Task Manager in Python
====================

A simple, command-line task manager built with Python 3. The app allows users to add, view, edit, delete, and mark tasks as completed. It uses a JSON file for persistent storage.

Features
--------
- **Add Tasks**: Add a new task with a description and optional due date.
- **View Tasks**: View a list of all tasks with their details (description, due date, and status).
- **Edit Tasks**: Edit the task description or due date.
- **Delete Tasks**: Delete tasks from the list.
- **Mark Tasks as Completed**: Update the status of a task to "completed".
- **Persistent Storage**: Tasks are saved in a JSON file so they persist across program restarts.

Requirements
------------
- Python 3.x (tested with Python 3.8+)

No external libraries are required for this project. It uses the built-in Python `json` and `os` modules.

Installation
------------
1. Clone this repository or download the source code.

   git clone https://github.com/finnBaldwin/task-manager-python3.git

2. Navigate into the project directory:

   cd task-manager-python

3. Make sure you have Python 3 installed. You can check your Python version by running:

   python --version

Usage
-----
### Running the Task Manager

To run the task manager, simply execute the following command in your terminal:

   python task_manager.py

You will be presented with a menu to interact with the task manager. The options are:

1. **Add Task**: Add a new task to your list.
2. **View Tasks**: View all your tasks.
3. **Edit Task**: Edit an existing task (description or due date).
4. **Delete Task**: Delete a task by ID.
5. **Mark Task as Completed**: Mark a task as completed.
6. **Exit**: Exit the program.

### Task JSON File

The tasks are stored in a JSON file called `tasks.json`. If the file doesn't exist, it will be created automatically. Here's an example of what the file looks like:

[
    {
        "id": 1,
        "description": "Complete Python project",
        "due_date": "2024-11-20",
        "status": "pending"
    },
    {
        "id": 2,
        "description": "Buy groceries",
        "due_date": "2024-11-15",
        "status": "completed"
    }
]

Project Structure
-----------------
task-manager-python/
│
├── task_manager.py         # Main Python script containing the task manager functionality
├── tasks.json              # JSON file for storing tasks (created automatically)
└── README.md               # This README file

Contributing
------------
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

Here are some ways you can contribute:
- Report bugs or issues.
- Improve documentation.
- Add new features (e.g., task priority, notifications, etc.).
- Improve code quality or refactor sections of the code.

License
-------
This project is open-source and available under the MIT License. See the LICENSE file for more details.

Acknowledgements
----------------
- Thanks to the Python community for building such a powerful and easy-to-use programming language!
