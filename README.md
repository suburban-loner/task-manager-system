# Task Manager System
This is a task management system where users can manage tasks assigned to them and admins can oversee all tasks and users. 

## Features
The task manager includes the following core functionalities:

## User Registration:
Users can register new users (admin access only).
The reg_user() function ensures that no duplicate usernames are registered.

## Adding Tasks:
Users can add new tasks, which are stored in tasks.txt.
The add_task() function allows users to define tasks with details like due date, assigned user, and task description.

## Viewing Tasks:
Users can view all tasks (view_all()) or only the tasks assigned to them (view_mine()).
Tasks are displayed with a number identifier, allowing users to easily select and modify tasks.

## Editing and Completing Tasks:
When viewing personal tasks using the view_mine() function, users can select a task to either mark it as complete or edit the task.
Tasks can only be edited if they have not been completed.

## Generating Reports:
## Admins can generate two types of reports:
task_overview.txt: Summarizes the overall task statistics, including total tasks, completed tasks, uncompleted tasks, overdue tasks, and percentages.
user_overview.txt: Summarizes user-specific statistics such as the number of tasks assigned, completed tasks, incomplete tasks, and overdue tasks.
Viewing Statistics:

Admin users can view statistics generated in the reports. If the reports have not been generated yet, the system will generate them automatically before displaying the statistics.
Updated Functionality
Functions
The code has been updated to use functions for improved modularity and readability. Some key functions include:

reg_user(): Registers a new user while ensuring usernames are unique.
add_task(): Allows users to add tasks to the system.
view_all(): Displays all tasks stored in tasks.txt in a readable format.
view_mine(): Shows only tasks assigned to the logged-in user and allows the user to edit or mark them as complete.
generate_reports(): Generates task and user reports, stored in task_overview.txt and user_overview.txt.
display_statistics(): Displays task statistics from the generated reports.
Enhanced Task Management

## When a user views their tasks (view_mine()), they can now:
Select a task to edit or mark as complete.
Only tasks that are incomplete can be edited.
Task editing allows for updating the assigned user or changing the task's due date.

## Reports
Task Overview (task_overview.txt)

### This report includes:
Total number of tasks.
Number of completed tasks.
Number of uncompleted tasks.
Number of overdue tasks.
Percentage of incomplete tasks.
Percentage of overdue tasks.
User Overview (user_overview.txt)
This report includes:
Total number of users.
Total number of tasks.

### For each user:
Total number of tasks assigned.
Percentage of tasks assigned to the user.
Percentage of tasks completed by the user.
Percentage of tasks still incomplete.
Percentage of incomplete tasks that are overdue.
