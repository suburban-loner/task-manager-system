import datetime


def reg_user(username, password, confirm_password):
    """This function takes in a username, password, and confirm password and checks if the username already exists in the
    user.txt file. If it does, it prints a message saying that the username already exists. If it doesn't, it checks if the
    password and confirm password match. If they do, it writes the username and password to the user.txt file. If they
    don't, it asks the user to confirm their password again
    :param username: the username of the user
    :param password: the password the user entered
    :param confirm_password: the password that the user inputs to confirm their password"""
    usr_f = open('user.txt', 'r+')
    usr_check = usr_f.readlines()
    users = []
    # The code is checking to see if the username already exists in the file. If it does, it will print a message
    # saying that the username already exists. If it doesn't, it will check to see if the password and confirm password
    # match. If they do, it will write the username and password to the file. If they don't, it will print a message
    # saying that the passwords do not match and ask the user to confirm the password again.
    for name in usr_check:
        user, pswd = name.strip('\n').split(', ')
        users.append(user)
    if username in users:
        print("Username already exists, please try again.")
    else:
        if confirm_password == password:
            usr_f.write(f"{username}, {password}\n")
            print("New user registered\n")
        else:
            print("Your passwords do not match")
            confirm_password = input("Confirm password:")
    usr_f.close()
    print("User successfully added")


def add_task(username, task, descrip_task, date, due_date, completed):
    """This function takes in a username, task, description of the task, date, due date, and whether the task is
    completed and adds it to the tasks.txt file
    :param username: The username of the person who created the task
    :param task: The name of the task
    :param descrip_task: This is the description of the task
    :param date: the date the task was created
    :param due_date: The date the task is due
    :param completed: True or False"""
    task_f = open('tasks.txt', 'a')
    task_f.write(f"{username}, {task}, {descrip_task}, {date}, {due_date}, {completed}\n")
    task_f.close()
    print("Task successfully added")


def view_all():
    """This function opens the tasks.txt file, reads all the lines, and then prints them out in a formatted way"""
    tsk_f = open('tasks.txt', 'r')
    all_tasks = tsk_f.readlines()
    tsk_f.close()
    for line in all_tasks:
        user, task, descrip_task, date, due_date, completed = line.strip('\n').split(', ')
        tasks = f"Task:\t\t\t\t{task}\nAssigned to:\t\t{user}\nDate assigned:\t\t{date}\nDue date:\t\t\t{due_date}\nTask complete?\t\t{completed}\n"
        print(tasks)


def view_mine(usr):
    """It allows the user to view their tasks, select a specific task, and edit the task.
    :param usr: the username of the user"""
    global string
    t_file = open('tasks.txt', 'r')
    t_checks = t_file.readlines()
    usrs = []
    task_list = []

    # The code is taking the text file and splitting it into a list of lists.
    for count, t in enumerate(t_checks):
        user, task, descrip_task, date, due_date, completed = t.strip('\n').split(', ')
        usrs.append(user)
        task_list.append([user, task, descrip_task, date, due_date, completed])

        # The code is printing the task, user, date, due date, completed, and description of the task.
        if usr == user:
            string = f"{count}. Task:\t\t\t{task}\nAssigned to:\t\t{user}\nDate assigned:\t\t{date}\nDue date:\t\t\t{due_date}\nTask Complete?\t\t{completed}\nTask description:\n {descrip_task}\n "
            print(string)

    print(task_list)
    # The code is asking the user to input a number corresponding to a specific task or enter '-1' to return to main
    # menu.
    specify = input("Enter a number corresponding to a specific task or enter '-1' to return to main menu: ")

    # Asking the user to input a number and if the number is -1, it will print "Exit code confirmed"
    if specify == '-1':
        print("Exit code confirmed")

    selection = task_list[int(specify)]

    sub_menu = input(
        "Select one of the following\nm - mark the task as complete\ne - edit the task\nSelection: ").lower()

    task_override = open('tasks.txt', 'w')

    # Writing the task list to the file.
    if sub_menu == 'm':
        task_list[int(specify)][-1] = 'Yes'
        print("You have marked task as completed")
        print(task_list[int(specify)])
        for t in task_list:
            task_override.write(", ".join(t) + '\n')
        print(", ".join(task_list[int(specify)]))

    # Changing the username of the task that the user has specified.
    if sub_menu == 'e':
        if completed == 'No':
            edit = input("What would you like to edit?\nu - username\ndd - due date\nSelection: ").lower()
            if edit == 'u':
                new_usr = input("Enter a new username:")
                task_list[int(specify)][0] = new_usr
                print("Username changed")
                # Writing updated task list to file
                for t in task_list:
                    task_override.write(", ".join(t) + '\n')

            # The code is changing the due date of the task.
            elif edit == 'dd':
                new_dd = input("Enter new due date(day-mon-year):")
                task_list[int(specify)][-2] = new_dd
                print("Due date changed")
                # Writing updated task list to file
                for t in task_list:
                    task_override.write(", ".join(t) + '\n')

    task_override.close()


def generate_reports():
    # ====Task Overview====
    task_file = open('tasks.txt', 'r')
    t_check1 = task_file.readlines()
    task_file.close()
    num_of_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    # The above code is reading the file and splitting the lines into the variables.
    for line in t_check1:
        user, task, descrip_task, date, due_date, completed = line.strip('\n').split(', ')
        num_of_tasks += 1

        if completed == "Yes":
            completed_tasks += 1
        else:
            uncompleted_tasks += 1

        # The above code is checking if the task is completed or not. If the task is not completed,
        # it will check if the due date is less than the current date. If it is, it will add 1 to the
        # incomplete_tasks variable. If the due date is not less than the current date, it will add 1 to the
        # overdue_tasks variable.
        if completed == "No":
            if due_date < date:
                incomplete_tasks += 1
            else:
                overdue_tasks += 1

    # The above code is calculating the percentage of incomplete tasks.
    incomplete_percentage = (incomplete_tasks / num_of_tasks) * 100
    incomplete_percentage = round(incomplete_percentage, 3)
    # The above code is calculating the percentage of overdue tasks.
    overdue_percentage = (overdue_tasks / num_of_tasks) * 100
    overdue_percentage = round(overdue_percentage, 3)

    # The above code is using the f-string method to print out the values of the variables.
    statement = f"Tasks generated: {num_of_tasks}\nCompleted tasks: {completed_tasks}\nUncompleted tasks: " \
                f"{uncompleted_tasks}\nOverdue tasks: {overdue_tasks}\nTasks that are incomplete: " \
                f"{incomplete_percentage}%\nTasks that are overdue: {overdue_percentage}% "

    # Opening a file called task_overview.txt and writing to it.
    task_output = open('task_overview.txt', 'w')
    task_output.write(statement)
    task_output.close()

    # ====User Overview====
    user_file = open('user.txt', 'r')
    u_check = user_file.readlines()
    user_file.close()
    task_file = open('tasks.txt', 'r')
    t_check = task_file.readlines()
    task_file.close()

    users = []
    num_of_users = 0
    users_tasks = 0
    complete_users = 0
    uncomplete_users = 0
    incomplete_users = 0
    overdue_users = 0

    # The above code is taking the user_check.txt file and splitting it into two parts, the username and the
    # password.
    for name in u_check:
        user, pswd = name.strip('\n').split(', ')
        num_of_users += 1
        users.append(user)

    # The above code is taking the task_file and splitting it into a list of lists.
    for name in t_check:
        user, task, descrip_task, date, due_date, completed = name.strip('\n').split(', ')
        # This is checking if the task is completed or not. If the task is not completed, it will check if
        # the due date is less than the current date. If it is, it will add 1 to the incomplete_tasks
        # variable. If the due date is not less than the current date, it will add 1 to the overdue_tasks
        # variable.
        if completed == 'Yes':
            complete_users += 1
        else:
            uncomplete_users += 1
        if due_date > date:
            overdue_users += 1

    # This is opening a file called user_overview.txt and writing to it.
    user_output = open('user_overview.txt', 'w')
    user_output.write(f"Users registered: {num_of_users}\nTasks generated: {num_of_tasks}\n\n")

    # This is checking if the user is in the list of users. If the user is in the list of users, it will add
    # 1 to the user_tasks variable. If the user is in the list of users, it will check if the task is
    # completed or not. If the task is completed, it will add 1 to the complete_user variable. If the task is
    # not completed and the due date is greater than the current date, it will add 1 to the overdue_user
    # variable. If the task is not completed, it will add 1 to the incomplete_user variable.
    for name in users:
        user_tasks = 0
        complete_user = 0
        incomplete_user = 0
        overdue_user = 0
        for line in t_check:
            user, task, descrip_task, date, due_date, completed = line.strip('\n').split(', ')
            if name == user:
                user_tasks += 1
                if completed == "Yes":
                    complete_user += 1
                elif complete_user == "No" and due_date > date:
                    overdue_user += 1
                elif completed == "No":
                    incomplete_user += 1

        # This is checking if the number of tasks is greater than 0. If it is, it will calculate the
        # percentage of tasks assigned to the user.
        if num_of_tasks > 0:
            user_per = round((user_tasks / num_of_tasks) * 100, 2)

        # This is checking if the number of tasks is greater than 0. If it is, it will calculate the
        # percentages needed.
        complete_per = 0
        incomplete_per = 0
        overdue_per = 0
        if user_tasks > 0:
            complete_per = round((complete_user / user_tasks) * 100, 2)
            incomplete_per = round((incomplete_user / user_tasks) * 100, 2)
            overdue_per = round((overdue_user / user_tasks) * 100, 2)

        statement2 = f"User '{name}' has {user_tasks} tasks assigned to them.\n{user_per}% of the " \
                     f"tasks are assigned to '{name}'.\nCompleted tasks: {complete_per}%\n" \
                     f"Incomplete tasks: {incomplete_per}%\nOverdue tasks: {overdue_per}%\n\n"
        user_output.write(statement2)
    user_output.close()


# ====Login Section====

# This is creating a list of usernames and passwords from the user.txt file.
username_list = []
password_list = []
user_file = open('user.txt', 'r')
user_check = user_file.readlines()
user_file.close()
# The code is taking the user_check list and splitting it into two lists, one for the username and one for the
# password.
for name in user_check:
    user, pswd = name.strip('\n').split(', ')
    username_list.append(user)
    password_list.append(pswd)

print("Login below:\n")
usr = input("Enter your username:")
pwd = input("Enter your password:")

while True:
    if usr in username_list:
        pswd_pos = username_list.index(usr)
        if password_list[pswd_pos] == pwd:
            print("logged in")
            break
        else:
            print("Wrong password")
            pwd = input("Enter your password:")
    else:
        print("Wrong username and/or password")
        usr = input("Enter your username:")
        pwd = input("Enter your password:")

print(" ")
while True:
    while usr == 'admin':
        menu = input("Please select one of the following options:\nr - register user\na - add task\nva - view all "
                     "tasks\nvm -view my tasks\ngr - generate reports\nds - display statistics\ne - exit\nSelection: "
                     "").lower()
        print(" ")

        if menu == 'r':
            # This is asking the user to enter a new username, password and confirm password. It is then calling the
            # reg_user function and passing the username, password and confirm password as arguments.
            username = input("Enter a new username:")
            password = input("Enter a new password:")
            confirm_password = input("Confirm password:")
            reg_user(username, password, confirm_password)

        # The above code is asking the user to input the username, task, description of the task, due date, date, and
        # completed.
        elif menu == 'a':
            username = input("Enter the username:")
            task = input("Enter task you are assigning to user:")
            descrip_task = input("Enter a description of the task:")
            due_date = input("When is the due date for the task?(day-mon-year):")
            date = datetime.date.today().strftime("%d-%b-%Y")
            completed = "No"
            add_task(username, task, descrip_task, date, due_date, completed)

        # This is calling the view_all function and printing all the tasks in the tasks.txt file.
        elif menu == 'va':
            view_all()

        # Asking the user to enter their username, and then it will display the user's messages.
        elif menu == 'vm':
            view_mine(usr)

        elif menu == 'ds':
            # Calling the function generate_reports()
            generate_reports()
            # Opening the file task_overview.txt and reading the lines in the file.
            t_overview = open('task_overview.txt', 'r')
            t_o_check = t_overview.readlines()
            t_overview.close()
            # Opening the file user_overview.txt and reading the lines in the file.
            u_overview = open('user_overview.txt', 'r')
            u_o_check = u_overview.readlines()
            u_overview.close()

            print("Task Overview:")
            for task in t_o_check:
                task = task.strip('\n')
                print(task)

            print(" ")

            # Printing the user overview.
            print("User Overview:")
            for user in u_o_check:
                user = user.strip('\n')
                print(user)

        elif menu == 'gr':
            # Calling the function generate_reports()
            generate_reports()
            print("Reports generated!!")

        elif menu == 'e':
            # Exiting the loop when user selects e.
            print("Goodbye!!!")
            exit()

        else:
            print("Invalid entry. Try again")

    while usr != 'admin':
        menu_in = "Please select one of the following options:\na - add task\nva - view all tasks\nvm - view my " \
                  "tasks\ne - exit\nSelection: "
        menu = input(menu_in).lower()
        print(" ")

        # The code is asking the user to input the username, task, description of the task, due date, date, and
        # completed.
        if menu == 'a':
            username = input("Enter the username:")
            task = input("Enter task you are assigning to user:")
            descrip_task = input("Enter a description of the task:")
            due_date = input("When is the due date for the task?(day-mon-year):")
            date = datetime.date.today().strftime("%d-%b-%Y")
            completed = "No"
            add_task(username, task, descrip_task, date, due_date, completed)

        elif menu == 'va':
            # Calling function view_all
            view_all()

        elif menu == 'vm':
            # Calling function view_mine
            view_mine(usr)

        elif menu == 'e':
            print("Goodbye!!!")
            exit()

        else:
            print("Invalid entry. Try again")
