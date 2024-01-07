#Declaration of variables
access = False      #It is used to evaluate the login
balance = 2000      #Initial balance
answer = "y"        #It is used to evaluate the return to the main menu
add_money = 0
minus_money = 0

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

menu_02 = """
1. To Deposit
2. To Withdraw
3. To view balance
4. Transfer money
5. Exit
"""

#Outgoing message
def message_goodbye():
    print("Come back soon.\nThank you :)")
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
    return access

#Function to perform operations with the balance
def options(number_operation, total_money, money_in, money_out):
    if number_operation == "1":
        print("\nHow much are you going to deposit?: ")
        money_in = input("$ ")
        money_in = int(money_in)
    elif number_operation == "2":
        print("\nHow much are you going to withdraw?: ")
        money_out = input("$ ")
        money_out = int(money_out)
    elif number_operation == "3":
        print("\nAvailable balance:")
        print(total_money)
    elif number_operation == "4":
        user_transfer = input("\nWho are you going to transfer money to?: ")
        print("\nHow much are you going to transfer?: ")
        money_out = input("$ ")
        money_out = int(money_out)
        print(f"\nSuccessful operation, {user_transfer} has received a transfer of $ {money_out}")
    total_money = total_money + money_in - money_out
    return total_money

print(menu_01)
access = login_user()

if access == True:
    while answer == "y" or answer == "yes":
        print("*****************************\n")
        print("What operation do you want to do?")
        print(menu_02)
        n_operation = input("Please, choose a number from 1 to 5 (1-5): ")
        if n_operation == "1" or n_operation == "2" or n_operation == "3" or n_operation == "4":
            balance = options(n_operation, balance, add_money, minus_money)
            answer = input("\nDo you want to do another operation? (y/n): ")
            answer = answer.lower()
        elif n_operation == "5":
            message_goodbye()
            answer = "n"
        else:
            print("Warning: Incorrect operation number")
            message_goodbye()
            answer = "n"
    if answer == 'n' or answer == 'no':
        message_goodbye()
else:
    print("Warning: Maximum number of attempts")
    print("Locked system")
    message_goodbye()