

#=====importing libraries===========
  
#No library to import 

#====Login Section====

#Use of while loop for program

while True:
    
# User to input username
 username_input=input("Please enter your username:\n")
# user to input password 
 password_input=input("Please enter your password:\n")
 # Emty list for username
 username=[]
 # Empty list for password
 password=[]
    
    
 # Open user.txt file
 # Reads the username and password from user.txt file
 # Presents data on seperate lines 
 with open ('user.txt','r') as f:
     login_data = f.readline().strip().split(",")
     username.append(login_data[0])
     password.append(login_data[1])
     admin_user= "".join(username)
     admin_password= "".join(password).lstrip()

    
               
   # If statment ensure that only the admin login to the menu selection
   # Else the user will be re-directed to user name and password input
    
     if (username_input != admin_user) or (password_input != admin_password): 
         print("Your credentials are incorrect, please re-enter\n")
         continue
     else:   
         print("This login information is correct, please see menu below")
         break
           
    
print("\n")      

# Use of while loop for menu                        
while True:
    
    print("\n")
    
    # User to select from menu presented below 
    # Make sure that the user input is converted to lower case  
    menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all task
vm - View my tasks
m- View total task and users
e  - Exit:''').lower()
    
    print("\n")                 

    # Admin user enters 'r' in menu 
    if menu == 'r':  
                 pass
              
                  # Admin user to enter the new username for registration
                 new_username=input("Please enter a new username:\n")
                  # Admin user to enter the new password for registration
                 new_password=input("Please enter a new password:\n")
                  # Admin user to enter password for confirmation
                 confirm_password= input("Please confirm password:\n")
                  
                 
                # If statement to ensure password and confirm password match
                # New username and password appended to user.txt
                # Else admin user must re-enter password 
                 if confirm_password==new_password:
                      print("Your login has been verified.")
                      #New username and password appended to user.txt
                      with open ('user.txt','a') as f:
                        f.write("\n"+new_username+","+confirm_password)  
                 else :
                     print("Password incorrect, please try again")
                     
                  
    #User enters 'a' in menu                   
    elif menu == 'a':
                   pass
                   # Open and appends task data to tasks.txt to add new tasks
                   with open('tasks.txt','a') as f:
                    # User to enter name of user task is assigned to
                    task_assign=input("Assigned to:")
                    # User to enter a task
                    task_title=input("Task:")
                    # User to enter a description of the task
                    task_description=input("Task description:")
                    # User to enter the due date of task
                    due_date=input("Due date:")
                    # User to enter the currrent date
                    current_date=input("Current date:")
                    # User to enter whether the task has been completed
                    task_complete=input("Task complete:")
                    
                    # compile all user input into variable task_info
                    # Write task_info in tasks.txt
                    task_info=task_assign+ "," +task_title+ "," +task_description+ "," +due_date+ "," +current_date+ "," + task_complete
                    f.write("\n"+ task_info)
                    
    #User enters 'va' in menu       
    elif menu == 'va':
                   pass
                   # Open tasks.txt to disaplay all tasks
                   # Use for loop to index all task inputs from 'a' section
                   # Display all tasks in a user-friendly manner
                   with open('tasks.txt','r') as display_file:
                       for line in display_file.readlines():
                           display_line= line.strip().split(",")
                           task_display=("Assigned to:"+" "+display_line[0]+"\n"+"Task:"+" "+display_line[1]+"\n"+"Due date:"+" "+display_line[3]+"\n"+"Current date:"+" "+display_line[4]+"\n"+"Task Complete?"+" "+display_line[5]+""+"\n"+"Task description:"+"\n"+display_line[2])
                           print(task_display+"\n")

   # User enters 'vm' in menu
    elif menu == 'vm':
                   pass
                   # Opens tasks.txt
                   # Use for loop to index all tasks inputs from 'a' section
                   with open('tasks.txt','r') as display_file:
                       for line in display_file.readlines():
                           display_line= line.strip().split(",")
                           task_display=("Assigned to:"+" "+display_line[0]+"\n"+"Task:"+" "+display_line[1]+"\n"+"Due date:"+" "+display_line[3]+"\n"+"Current date:"+" "+display_line[4]+"\n"+"Task Complete?"+" "+"No"+"\n"+"Task description:"+"\n"+display_line[2])
                           
                           # User to enter the username
                           # If username corresponds with username assignned to a task 
                           # Print out all task info associtated with inputted username
                           username_input=input("Please enter a username:\n")
                           if username_input == display_line[0]:
                               print(task_display)
                               break
   # User enter 'm' in menu                   
    elif menu == "m":
                  pass
                  # Open tasks.txt 
                  # Use of for loop to count the amount of task are present in tasks.txt
                  # Print out total number of task 
                  with open('tasks.txt','r') as task_menu:
                      total_task=0
                      for i in task_menu:
                         total_task += 1
                      print(f"The total number of tasks is:{total_task}\n")
                         
                  # Open user.txt
                  # Use for loop to count the amount of user are present in user.txt
                  # Print out total users 
                  with open('user.txt.','r') as user_menu:
                     total_user=0
                     for i in user_menu:
                         total_user += 1
                     print(f"The total number of users is:{total_user}")
                     
    # User enter 'e' in menu 
    # Exist program
    elif menu == 'e':
                    print('Goodbye!!!')
                    exit()
    # user entry not present in menu 
    else:
           print("You have made a wrong choice, Please Try again")