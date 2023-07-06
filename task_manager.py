#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime 

#====Login Section==

# user.txt reads the file 
# created 2 empty list to store new usernames and passwords 
user_names = []
pass_words = []

# for loop, loops through the lines and adds new usernames and passwords to list 
file = open("user.txt","r")
for line in file.readlines():
    
    Lines = line.strip()
    Lines = Lines.split(", ") 
    user_names.append(Lines[0])
    pass_words.append(Lines[-1])

# while login = to false userName and password will be printed out 
login = False
while login == False:
    
     user_name = (input("Please enter a username: "))
     user_pass = (input("Please enter a password: "))

# if above is not true below will be false and message will be printed out 
     if user_name in user_names and user_pass in pass_words:
         
        print(user_name, "has successfully logged in")
        login = True
        break
     else:
        print(" invalid log in details ")

# the program will continue to run as the condition is met
while True:
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - display statistics of total number of task and users in txt
e - Exit
''').lower()

# if user selects r username and password will be asked to be enterd.  
# if password is equal to confirm they will be added to user file in user.txt  
    if menu == 'r':
        if user_name == "admin":
            new_user_login = False
            
            while new_user_login == False:
                
                new_username = input("Enter your username : ")

                if new_username in user_names:
                    print("UserName is taken")
                else:
                    new_user_login=True
                    
            while new_user_login == True:
                new_user_pass = input("Enter a password:")

                check = input("confirm password:")
                if new_user_pass == check:
                    new_user_login = False
                    print(new_username," is offically registered" ) 
                    f = open("user.txt","a")
                    f.write(f"\n{new_username}, {new_user_pass}")
                    f.close()
                else :
                    print("password do not match. try again!")
        else:
            print("only the admin is allowed to add a new user")

 # if "a" is selected (tasks.txt) will opend and ask user a set of questions       
 # After that the file will close 
    elif menu == 'a':
            file = open("tasks.txt","a+")
            Task = input("Enter the username of the asignee: ")
            Title = input("what is the title of your task ?: ")
            Description = input("what does your task do ?: ")
            Due_Date = input("What date is your task due YYYY-MM-DD ?: ")
            Date = datetime.datetime.now().date()
            Completed = "No" 
            file.write('\n'+ str(Task) + "," + str(Title) + "," + str(Description) + "," + str(Due_Date) + "," + str(Date) + "," + str(Completed))
            file.close()

# if "va" is selected All task wll be read in a set format. 
    elif menu == 'va':
        with open("tasks.txt","r+") as f:
            task_list = []
            for line in f.readlines():
                Lines = line.strip()
                Lines = line.split(",")  
                task_list.append(Lines)
                 
                for task in task_list:
                    print("Task asigned to :\t ", task[0])
                    print("Title :\t \t \t",task[1])
                    print("Description :\t \t", task[2])
                    print("Due Date :\t \t", task[3])
                    print("Date :\t \t \t", task[4])
                    print("Completed ?: \t \t ", task[5])
                    
 # if "vm" is selected username enterd in login above is equal to tasks.txt.
 # Then the below will only print out the task assigned by tasks.txt
    elif menu == 'vm':
        with open ("tasks.txt","r+") as files:
            tasks_files = []
            for line in files.readlines():
                T_file = line.strip() 
                T_file = line.split(",")
                tasks_files.append(T_file)
                
            for tasks in tasks_files:    
                if user_name == tasks[0]:
                    print("welcome:",tasks[0]) 
         
                    print("Task:\t \t \t",tasks[1])
                    print("Assigned to:\t \t",tasks[0])
                    print("Date assigned:\t \t",tasks[3])
                    print("Due Date:\t \t",tasks[4])
                    print("Task Completed ?:\t",tasks[5])
                    print("Task Descrption:\t",tasks[2])
                     
# if user selects "s" task file and user file will open.
# it will count the number of users and the number of tasks and close both files 
    elif menu == "s":
        if user_name == "admin":
            tasks_file = open("tasks.txt", "r")
            count = 0 
            for line in tasks_file : 
                count = count+1 
            print(f"There are {count} tasks")
            tasks_file.close()     
          
        user_file = open("user.txt", "r")
        count = 0
        for line in user_file:
            count+=1
        print(f" There are {count} users")    
         
        user_file.close()       

# program will exit if "e" is selected.
# display a appropriate error message if user enters a wrong choice   
    elif menu == 'e':
        print('Goodbye!!!')
        exit()   
    else:
     print("You have made a wrong choice, Please Try again")

        
    