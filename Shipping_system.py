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
        print(f"\nAttempt {i+1} of {number_attempts}")
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
    weight = input("Enter the weight of the package: ")
    weight = float(weight)
    weight = round(weight, 2)
    while weight <= 0:
        print("\nWarning: wrong Weight")
        weight = input("Enter the weight of the package: ")
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
    Weight: {weight_in}
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
menu_02 ="""
You have two options:
1- Send
2- Exit

"""






