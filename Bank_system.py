menu_01 = """
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
print(menu_01)

access = False
balance = 2000

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

menu_02 = """
1. To Deposit
2. To Withdraw
3. To view balance
4. Transfer money
5. Exit
"""
answer = "y"
add_money = 0

def options(number_operation, balance):
    if number_operation == "1":
        print("\nHow much are you going to deposit?: ")
        add_money = input("$ " )
        add_money = int(add_money)
    elif number_operation == "2":
        print("\nElegiste 2")
    elif number_operation == "3":
        print("\nAvailable balance:")
        print(balance)
    elif number_operation == "4":
        print("\nElegiste 4")
    balance_final = balance + add_money
    
if access == True:
    while answer == "y" or answer == "yes":
        print("*****************************\n")
        print("What operation do you want to do?")
        print(menu_02)
        n_operation = input("Please, choose a number from 1 to 5 (1-5): ")
        if n_operation == "1" or n_operation == "2" or n_operation == "3" or n_operation == "4":
            options(n_operation, balance)
            answer = input("\nDo you want to do another operation? (y/n): ")
            answer = answer.lower()
        elif n_operation == "5":
            print("\nCome back soon.\nThank you :)\n")
            print("\n*****************************\n")
            answer = "n"
        else:
            print("Warning: Incorrect operation number")
            print("Come back soon.\nThank you :)")
            print("\n*****************************\n")
            answer = "n"

else:
    print("Warning: Maximum number of attempts")
    print("Locked system")
    print("Come back soon.\nThank you :)")
    print("\n*****************************\n")




