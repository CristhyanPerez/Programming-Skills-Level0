#Import the libraries
import os
import csv

#Declaration variables
available_cities = ["London", "Manchester", "Liverpool"]
available_programs = ["Computer Science", "Medicine", "Marketing", "Arts"]
available_options = ["1", "2", "3", "4"]
access_login = False

#Program exit message
def message_goodbye(sentence):
    print(sentence)
    print("Thank you")
    print("\n*****************************\n")

#Function to evalauate the three access attempts
def login_user():
    for i in range (0,3):
        username = input("What is your username?: ")
        number_char = len(username)
        password_system = username + " " +  str(number_char)
        password_input = input("What is your password?: ")
        print(f"\nAttempt {i + 1} of 3")
        if password_input == password_system:
            print("Correct username and password\n")
            access = True
            break
        else:
            print("Warning: Incorrect password...")
            if i < 2:
                print("Reset username and pasword\n")
                print("********** Log in **********\n")
                access = False
    return access

#Funtion to verify the existence of .csv file. If it doesn't exist, it's created
def file_exists():
    file_csv_exists = os.path.isfile('enrollment.csv')
    if not file_csv_exists:
        with open('enrollment.csv', 'w') as file:
            file.write('')

#Function to place student data in a list
def student_list(name, last_name, program, city):
    student_data = [0,0,0,0]
    student_data[0] = name
    student_data[1] = last_name
    student_data[2] = program
    student_data[3] = city
    return student_data

#Welcome message
menu_01 = """
Welcome to the university enrollment system:

Notes:
*The password is made up of the following:
Username + space + number of characteres in the user word

Example:
Username: Cris
Password: Cris 4

*You will only have three attempts.

**************  Log in  **************
"""

#Country Options
menu_02 = """
Availables Cities
1. London
2. Manchester
3. Liverpool"""

#Program Options
menu_03 = """
Availables programs:
1. Computer Science
2. Medicine
3. Marketing
4. Arts
"""

file_exists()
print(menu_01)
access_login = login_user()

if access_login == True:
    #SHow the initial menu and request registration information
    print("***********  Welcome again  ***********\n")
    print("You have the following information to be able to register: ")
    print(menu_02)
    print(menu_03)
    name = input("What's your name?: ")
    last_name = input("What's your last name?: ")
    chosen_city = input("In which of the three cities do you want to enroll?(1-3): ")
    chosen_program = input("What program will you choose?(1-4): ")
    #Validate input data
    if chosen_city in available_options[0:3] and chosen_program in available_options[0:4]:
        chosen_city = int(chosen_city)
        chosen_program = int(chosen_program)
        student_to_enroll = student_list(name, last_name, available_programs[chosen_program - 1], available_cities[chosen_city - 1])
        print(student_to_enroll)
        print("Todo_gucci")
    else:
        message_goodbye("\nWarning: Wrong option chosen")   
else:
    print("\nWarning: Maximum number of attempts")
    message_goodbye("Locked system.")