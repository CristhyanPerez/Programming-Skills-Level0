#Import the libraries
import os
import csv
import pandas as pd

#Declaration variables
available_cities = ["London", "Manchester", "Liverpool"]
available_programs = ["Computer Science", "Medicine", "Marketing", "Arts"]
available_options = ["1", "2", "3", "4"]
slots_cities = [1, 3]
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
    file_csv_exists = os.path.isfile("enrollment.csv")
    if not file_csv_exists:
        with open("enrollment.csv", "w") as file:
            file.write('')
        
#Function to add values to csv file
def add_values_csv(path, data_list):
    with open(path, "a", newline = "") as file_csv:
        write_csv = csv.writer(file_csv, delimiter = "\t")
        write_csv.writerow(data_list)

#Function to place student data in a list
def student_list(name, last_name, program, city):
    student_data = [0,0,0,0]
    student_data[0] = name
    student_data[1] = last_name
    student_data[2] = program
    student_data[3] = city
    return student_data

#Slots available per program in each city
def number_slots_available(dataframe, program):
    df_program_london = dataframe[(dataframe["program"] == program) & (dataframe["city"] == "London")]
    df_program_manchester = dataframe[(dataframe["program"] == program) & (dataframe["city"] == "Manchester")]
    df_program_liverpool = dataframe[(dataframe["program"] == program) & (dataframe["city"] == "Liverpool")]
    slots_available_london = 1 - len(df_program_london)
    slots_available_manchester = 3 - len(df_program_manchester)
    slots_available_liverpool = 1 - len(df_program_liverpool)
    return slots_available_london, slots_available_manchester, slots_available_liverpool

#Function to check if there are places available for the chosen program
def check_availability(dataframe, program, city):
    dataframe_filtered = dataframe[(dataframe["city"] == city) & (dataframe["program"] == program)]
    print(dataframe_filtered)               #Para verificar que columnas está tomando
    if city == "London" or city == "Liverpool":
        number_max_program = slots_cities[0] #1 slot available
    elif city == "Manchester":
        number_max_program = slots_cities[1] #3 slot available
    #Count the number of registered
    number_students = len(dataframe_filtered)
    #Check if it exceeds the slots
    if number_students <= number_max_program:
        check = True    
    else:
        check = False
    return check 

#print slots availability message
def print_available_slots(dataframe, program, cities_list):
    av_london, av_manchester, av_liverpool = number_slots_available(dataframe, program)
    available_list = [0, 0, 0]
    available_list[0] = av_london
    available_list[1] = av_manchester
    available_list[2] = av_liverpool
    count = 0
    if av_london == 0 and av_london == 0 and av_london and 0:
        print(f"\nThere are no slots available in any city for the {program} program")
    else :
        print(f"\nFor the {program} program:")
        for i in available_list:
            if i <= 0:
                continue
            else:
                print(f"* {i} slot/s available in {cities_list[count]}")
            count = count + 1
        
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
path_csv_file = os.path.join(os.path.dirname(__file__), "enrollment.csv")
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
        add_values_csv(path_csv_file, student_to_enroll)
        #Transform the csv file into a pandas dataframe to be able to manipulate it better
        dataframe_enrollment = pd.read_csv("enrollment.csv", names = ["name", "last_name", "program", "city"], sep="\t")
        #Validate if there are places available in the chosen city
        validate = check_availability(dataframe_enrollment, student_to_enroll[2], student_to_enroll[3])
        if validate == True:
            print(f"\nCongratulations {student_to_enroll[0]}\n")
            print(f"You have enrolled in the program of {student_to_enroll[2]} in the city of {student_to_enroll[3]}")
        else:
            print(f"\nWe're sorry {student_to_enroll[0]}\n")
            print(f"There aren't places available in {student_to_enroll[3]} for the {student_to_enroll[2]} program")
            #To proceed to delete the last row
            last_row = dataframe_enrollment.index[-1]
            dataframe_enrollment = dataframe_enrollment.drop(last_row)
            
            #Show were there are places available for that program
            print_available_slots(dataframe_enrollment, student_to_enroll[2], available_cities)
        print("Todo_gucci")
    else:
        message_goodbye("\nWarning: Wrong option chosen")   
else:
    print("\nWarning: Maximum number of attempts")
    message_goodbye("Locked system.")