#Import the libraries
import os
import csv
import pandas as pd

#Declaration variables
available_cities = ["London", "Manchester", "Liverpool"]
available_programs = ["Computer Science", "Medicine", "Marketing", "Arts"]
available_options = ["1", "2", "3", "4"]

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
    for i in range(3):
        if list_slots_available[i] == 0:
            message = "There aren't slots available"
        elif list_slots_available[i] == 1:
            message = "There is a slot available"
            option = str(i + 1) 
            new_list_options.append(option)
        else:
            message = "There are " + list_slots_available[i] + " slots available"
            new_list_options.append(option)
        print(f" {i + 1} |  {list_cities[i]}:  {message}")
    return new_list_options

#Funtion to collect user data
def user_data(program, city):
    list_user = []
    name = input("What is your name?: ")
    last_name = input("What is your last name?: ")
    list_user.append(name)
    list_user.append(last_name)
    list_user.append(city)
    return list_user

