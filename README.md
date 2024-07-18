# Task Management System

A simple console-based Task Management System implemented in Python. This project allows users to add, view, update, delete, and mark tasks as completed. Tasks are saved to a file for persistence.

## Features

- Add new tasks with a title, description, due date, and priority.
- View all tasks with their details.
- Update existing tasks.
- Delete tasks.
- Mark tasks as completed.
- Persistent storage of tasks using a text file.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/task-management-system.git
    ```

2. Navigate to the project directory:
    ```sh
    cd task-management-system
    ```

3. Run the script:
    ```sh
    python task_manager.py
    ```

## Usage

1. When you run the script, you will be presented with a menu:

    ```
    ========================================
     Task Management System 
    ========================================
    1. Add Task
    2. View Tasks
    3. Update Task
    4. Delete Task
    5. Mark Task as Completed
    6. Exit
    ========================================
    Enter your choice: 
    ```

2. Choose an option by entering the corresponding number.

3. Follow the prompts to add, view, update, delete, or mark tasks as completed.

## File Structure

- `task_manager.py`: The main script containing the Task Management System code.
- `tasks.txt`: The file where tasks are saved. This file is created automatically when you run the script for the first time.

## Example

Here’s an example of how the Task Management System looks in action:

    ```
    ========================================
     Task Management System 
    ========================================
    1. Add Task
    2. View Tasks
    3. Update Task
    4. Delete Task
    5. Mark Task as Completed
    6. Exit
    ========================================
    Enter your choice:1
    Add Task
    Enter task title: Buy groceries
    Enter task description: Milk, eggs, bread
    Enter due date (YYYY-MM-DD): 2023-12-31
    Enter priority (Low/Medium/High): High
    Task added successfully.
    
    Press Enter to return to the main menu...
    ```

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any features, bug fixes, or enhancements.



