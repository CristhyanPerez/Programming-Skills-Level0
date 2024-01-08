#Declaration variables
available_countries = ["London", "Manchester", "Liverpool"]
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
Availables Countries
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

print(menu_01)
access_login = login_user()

if access_login == True:
    print("***********  Welcome again  ***********\n")
    print("You have the following information to be able to register: ")
    print(menu_02)
    print(menu_03)
    name = input("What's your name?: ")
    last_name = input("What's your last name?: ")
    chosen_country = input("In which country do you want to enroll?(1-3): ")
    chosen_program = input("What program will you choose?(1-4): ")
    if chosen_country in available_options[0:3] and chosen_program in available_options[0:4]:
        print("Todo Gucci")
    else:
        message_goodbye("\nWarning: Wrong option chosen")   
else:
    print("Warning: Maximum number of attempts")
    message_goodbye("Locked system.")