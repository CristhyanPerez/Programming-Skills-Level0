#Import the libraries
import os
import csv
import pandas as pd

#Declaration variables
available_cities = ["London", "Manchester", "Liverpool"]
available_programs = ["Computer Science", "Medicine", "Marketing", "Arts"]
available_options = ["1", "2", "3", "4"]
available_yes_no = ["yes", "y", "YES", "no", "n", "NO"]

#Define a function to check if the username and password are correct
def verify_log_in(username, password):
    lenght_username = len(username)
    password_system = username + " " + str(lenght_username)
    if password_system == password:
        return True
    else:
        return False

#Define function to vr¿erify log in in a defined number of attempts
def login_attempts(number_attempts):
    access_allowed = False
    for i in range(number_attempts):
        username_in = input("What is your username: ")
        password_in = input("What is your password: ")
        print(f"\nAttempt {i+1} of {number_attempts}\n")
        check_login = verify_log_in(username_in, password_in)   #True or False
        if check_login == True:
            access_allowed = True
            break
        else:
            print("\nWarning: Incorrect password")
            if i < ( number_attempts - 1 ):
                print("Reset username and pasword\n")
                print("********** Log in **********\n")
    return access_allowed

#Given a question and a list of answers, the function will evaluate if the
#answer to the question is within the list
def check_answer(question, list_answers):
    start_check = False
    while start_check == False:
        option_user = input(question)
        if option_user in list_answers:
            start_check = True
        else:
            print("Wrong option. Let's go again\n")
    return option_user

#Funtion to verify the existence of .csv file. If it doesn't exist, it's created
def file_exists(file):
    file_csv_exists = os.path.isfile(file)
    if not file_csv_exists:
        with open(file, "w") as file:
            file.write('')

#Funtion to transform the csv file into a pandas dataframe
def transform_dataset(file):
    dataframe = pd.read_csv(file, names = ["name", "last_name", "program", "city"], sep = "\t")
    return dataframe

#Function to call the dataset and filter by program, the number of available
#slots and the slots occupied by city
def number_slots_available(dataframe, program):
    df_program_london = dataframe[(dataframe["program"] == program) & (dataframe["city"] == "London")]
    df_program_manchester = dataframe[(dataframe["program"] == program) & (dataframe["city"] == "Manchester")]
    df_program_liverpool = dataframe[(dataframe["program"] == program) & (dataframe["city"] == "Liverpool")]
    slots_available_cities = []
    slots_available_london = 1 - len(df_program_london)         #There's only 1 slot available in london
    slots_available_manchester = 3 - len(df_program_manchester) #There's only 3 slot available in manchester
    slots_available_liverpool = 1 - len(df_program_liverpool)   #There's only 1 slot available in liverpool
    slots_available_cities.append(slots_available_london)
    slots_available_cities.append(slots_available_manchester)
    slots_available_cities.append(slots_available_liverpool)
    return slots_available_cities

#Function to show available slots by city
def show_slots_city(list_cities, list_slots_available, new_list_options):
    print("\nAvailability of the chosen program by city:\n")
    for i in range(3):
        if list_slots_available[i] == 0:
            message = "There aren't slots available"
        elif list_slots_available[i] == 1:
            message = "There is a slot available"
            option = str(i + 1) 
            new_list_options.append(option)
        else:
            message = "There are " + str(list_slots_available[i]) + " slots available"
            option = str(i + 1) 
            new_list_options.append(option)
        print(f"{i + 1}- {list_cities[i]}:  {message}")
    print()
    return new_list_options

#Function that receives a list and returns True if at least one of its elements is non-zero
def list_non_zero(number_list):
    elements = len(number_list)
    count = 0
    for i in range(elements):
        if number_list[i] != 0:
            count = count + 1
    if count ==  0:
        return False
    else:
        return True

#Funtion to collect user data
def user_data(program, city):
    list_user = []
    print("\nPersonal Information:\n")
    name = input("What is your name?: ")
    last_name = input("What is your last name?: ")
    list_user.append(name)
    list_user.append(last_name)
    list_user.append(program)
    list_user.append(city)
    return list_user

#Function to add values to csv file
def add_values_csv(file, data_list):
    path_csv_file = os.path.join(os.path.dirname(__file__), file)
    with open(path_csv_file, "a", newline = "") as file_csv:
        write_csv = csv.writer(file_csv, delimiter = "\t")
        write_csv.writerow(data_list)

#Function to choose program
def enrollment_program(menu, programs):
    print(menu)
    question = "What program do you want to enroll in? (1-4): "
    option_program = check_answer(question, available_options)
    index = int(option_program) - 1
    enroll_program = programs[index]
    return enroll_program

#Function to choose city
def enrollment_city(list_cities_available):
    question = "What city do you want to enroll in? (1-3): "
    option_city = check_answer(question, list_cities_available)
    index = int(option_city) - 1
    enroll_city = available_cities[index]
    return enroll_city

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Function to print the final summary with user data
def final_summary(enrollment_information):
    summary_final = f"""

    ****************    Final Summary    *********************

        Name:      {enrollment_information[0]}
        Last_name:    {enrollment_information[1]}
        Program:       {enrollment_information[2]}
        City:       {enrollment_information[3]}
    
    **********************************************************

    """
    print(summary_final)

#Menus
#Program entry menu
menu_entry = """
****************  Enrollment University  *********************

Welcome, first, you have to log in.

* The password is made up of the following:
  Username + space + number of characteres in the user word

Example:
Username: Cristhyan
Password: Cristhyan 9

Remember that you only have three attempts
"""

#Show available programs
menu_programs ="""
Available programs:

1- Computer Science
2- Medicine
3- Marketing
4- Arts
"""

#Main function
def main():
    print(menu_entry)
    login = login_attempts(3)
    if login == True:
        print("****************    Login Successfully   ********************")
        file_exists("enrollment.csv")
        df = transform_dataset("enrollment.csv")
        reset_main_menu = True
        new_list_options = []
        while reset_main_menu == True:
            print("\n**************************************************************\n")
            program_enroll = enrollment_program(menu_programs, available_programs)
            print()
            slots_program_city = number_slots_available(df, program_enroll)
            registration_possible = list_non_zero(slots_program_city)
            new_list_options = show_slots_city(available_cities, slots_program_city, new_list_options)
            if registration_possible == True:
                program_city = enrollment_city(new_list_options)
                user_list_data = user_data(program_enroll, program_city)
                final_summary(user_list_data)
                enroll = check_answer("\nAre you sure about enrolling?(y/n): ", available_yes_no)
                if enroll in available_yes_no[0:3]:
                    message_custom("\nSuccessful enrollment\n")
                    add_values_csv("enrollment.csv", user_list_data)
                    reset_main_menu = False
                else:
                    return_program = check_answer("\nDo you want to return to the main menu?(y/n): ", available_yes_no)
                    if return_program in available_yes_no[0:3]:
                        print("\nLet's start again..!!!!\n")
                        reset_main_menu = True
                    else:
                        message_custom("")
                        reset_main_menu = False
            else:
                print("\nAlert:\nThere aren't slots available for this program in any city\n")
                return_program = check_answer("\nDo you want to return to the main menu?(y/n): ", available_yes_no)
                if return_program in available_yes_no[0:3]:
                    print("\nLet's start again..!!!!\n")
                    reset_main_menu = True
                else:
                    message_custom("")
                    reset_main_menu = False
            new_list_options = []
    else:
        message_custom("Maximum number of attempts")

#Entry point
if __name__ == "__main__":
    main()