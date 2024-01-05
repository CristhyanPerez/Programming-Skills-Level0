menu = """
Welcome to the online Banking System:

Notes:
*The password is made up of the following:
Username + space + number of characteres in the user word

Example:
Username: Cris
Password: Cris 4

*You will only have three attempts.

********** Log in **********
"""
print(menu)

Access = False
balance = 2000

for i in range (0,3):
    username = input("What is your username?: ")
    number_char = len(username)
    password_system = username + " " +  str(number_char)
    password_input = input("What is your password?: ")
    print(f"\nAttempt {i + 1} of 3")
    
    if password_input == password_system:
        print("Correct username and password\n")
        Access = True
        break
    else:
        print("Warning: Incorrect password...")
        if i < 2:
            print("Reset username and pasword\n")
            print("********** Log in **********\n")

if Access == True:
    
    
else:
    print("Warning: Maximum number of attempts")
    print("Locked system")
    print("Come back soon.\nThank you :)")




