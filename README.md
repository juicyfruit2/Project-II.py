# Project-II.py

# Compulsory Task Part 1

This repository contains a program for managing tasks assigned to each member of a small business team. The program, `task_manager.py`, allows users to perform various actions such as logging in, registering a new user, adding tasks, and viewing tasks.

## Table of Contents

1. [Introduction](#introduction)
2. [Program Description](#program-description)
3. [Usage](#usage)
4. [Actions](#actions)
   - [Login](#login)
   - [Register a User](#register-a-user)
   - [Add a Task](#add-a-task)
   - [View All Tasks](#view-all-tasks)
   - [View My Tasks](#view-my-tasks)

## Introduction

In this task, we provide a template program (`task_template.py`) that serves as the foundation for building the task management program. The objective is to modify the template to fulfill the requirements outlined in the compulsory task.

## Program Description

The program interacts with two text files: `user.txt` and `tasks.txt`. These files store user credentials and task information, respectively.

- `user.txt`: Contains the usernames and passwords for each user who can access the program. Each line follows the format: `username, password`.
- `tasks.txt`: Stores a list of tasks assigned to team members. Each task is represented by a separate line and includes the following information:
  - Username of the assigned person
  - Task title
  - Task description
  - Task assignment date
  - Task due date
  - Completion status ('Yes' or 'No')

## Usage

To use the task management program, follow these steps:

1. Copy the provided template program, `task_template.py`, and save it as `task_manager.py` in the current folder.
2. Ensure the `user.txt` and `tasks.txt` files are present in the same folder as `task_manager.py`.
3. Run `task_manager.py` using a Python interpreter.
4. Follow the on-screen instructions and enter the required information to perform various actions.

Remember to save your work as you progress through the program.

## Actions

The program provides the following actions that users can perform:

### Login

- Users will be prompted to enter their username and password.
- The program will verify the credentials against the `user.txt` file.
- An appropriate error message will be displayed if the credentials are invalid.
- Users will be repeatedly prompted until valid credentials are provided.

### Register a User

- Only the user with the username 'admin' is allowed to register new users.
- After logging in as 'admin', selecting the 'r' option will prompt for a new username and password.
- Users will be asked to confirm the password, and if the confirmation matches, the new username and password will be added to `user.txt`.

### Add a Task

- After logging in, selecting the 'a' option will prompt for task details: assigned username, task title, task description, and due date.
- The program will add the new task to `tasks.txt` with the current date as the assignment date and 'No' as the completion status.

### View All Tasks

- After logging in, selecting the 'va' option will display all tasks in an easy-to-read format.
- Each task's information, including the assigned user, title, description, assignment date, due date, and completion status, will be shown.

### View My Tasks

- After logging in, selecting the 'vm' option will display tasks assigned to the currently logged-in user in a user-friendly manner.
- Only tasks assigned to the current user will be shown, including their information as described in the 'View All Tasks' section.

# Comp

# Compulsory Task Part 2

In this part of the task, we will introduce some formatting and additional features to the program.

## Formatting and Additional Features

1. Only the user with the username 'admin' is allowed to register new users.
2. The 'admin' user will have access to a new menu option, 's', which allows them to display statistics.
   - Selecting this option will display the total number of tasks and the total number of users in a user-friendly manner.

That concludes the changes made in Part 2 of the compulsory task. The program will now provide improved functionality and better user experience.

