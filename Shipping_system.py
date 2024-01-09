#Import libraries
import random

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

#Define funtion to store a person's data in a list
def list_person(role):
    print(f"The following information is requested from the {role}")
    list_user = [0, 0, 0]
    list_user[0] = input("*The name: ")
    list_user[1] = input("*The last name: ")
    list_user[2] = input("*The age: ")
    print()
    return list_user

#Define function assign the random number, and using the weight calculate the amount to pay
def amount_pay():
    number_random = random.randint(1000000, 9999999)
    weight = input("Enter the weight of the package(kg): ")
    weight = float(weight)
    weight = round(weight, 2)
    while weight <= 0:
        print("\nWarning: wrong Weight")
        weight = input("Enter the weight of the package(Kg): ")
        weight = float(weight)
        weight = round(weight, 2)
    print("\nThe rate is $2 per Kilogram\n")
    amount = 2 * weight
    return number_random, weight, amount

#Define a funtion to make a summary of the shipment
def summary_final(sender, recept, n_random, weight_in, amount_out):
    summary = f"""
    *************************  Summary  ***************************
    
    Data of Sender:
    Name: {sender[0]}, Last_name: {sender[1]}, Age: {sender[2]}
    
    Data of receptor:
    Name: {recept[0]}, Last_name: {recept[1]}, Age: {recept[2]}
    
    Data of package:
    Weight: {weight_in} Kg
    rate: $2/Kg

    The amount to pay is $ {amount_out}

    ***************************************************************
    """
    print(summary)

#Initial menu message
menu_01 = """
****************    Online Shipping System    *********************

Welcome, first, you have to log in.
Remember that you only have three attempts

"""

#Main menu
menu_02 ="""You have two options:
1- Send
2- Exit
"""

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

print(menu_01)
access_program = login_attempts(3)
if access_program == True:
    reset_main_menu = True
    while reset_main_menu == True:
        print(menu_02)
        chosen_option = input("Choose one of the two options (1-2): ")
        if chosen_option == "1":
            list_sender = list_person("sender")
            list_recipient = list_person("recipient")
            n_rand, weight_pack, amount_final = amount_pay()
            summary_final(list_sender, list_recipient, n_rand, weight_pack, amount_final)
            print("\nSuccessful shipment\n")
            other_operation = input("Do you want to perform another operation (y/n): ")
            if other_operation == "y" or other_operation == "yes":
                reset_main_menu = True
                print("\nLet's go back to the main menu\n")
            elif other_operation == "n" or other_operation == "no":
                reset_main_menu = False
                message_custom("It has been a pleasure to help you")
            else:
                reset_main_menu = False
                message_custom("Wrong option chosen")
        elif chosen_option == "2":
            reset_main_menu = False
            message_custom("It has been a pleasure to help you")
        else :
            reset_main_menu = False
            message_custom("Wrong option chosen")
else:
    message_custom("Maximum number of attempts")