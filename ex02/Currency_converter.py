#Declaration of variables
exchange_values = [892.86, 811.20, 1.00, 0.91, 29.82, 0.79, 3.69]
exchanges_symbols = ["CLP", "ARS", "USD", "EUR", "TRY", "GBP", "PEN"]
available_operation = ["1", "2", "3", "4", "5", "6", "7"]
available_answers = ["y", "yes", "Y", "YES", "n", "no", "N", "NO"]
reset = True
min_amount = 50
max_amount = 3000

#Funtion for outgoing message
def custom_message(sentence):
    print()
    print(sentence)
    print("Come back soon. Thanks")

#Funtion to evaluate the restart of the cycle
def reset_menu(reset_input):                        
    if reset_input in available_answers[0:4]:
        reset = True
        print("Let's start again\n")
        print("**********************************************\n")
    elif reset_input in available_answers[4:8]:
        reset = False
        custom_message("OK.!")
    else:
        reset = False
        custom_message("Sorry. Incorrect invalid answer.!!!")
    return reset

#Function to change dollars to another currency
def exchange_dolar_other(amount, value_exchange):
    amount = amount * value_exchange
    amount = round(amount, 2)
    return amount

#Funtion to change another currency to dollars
def exchange_other_dolar(amount, value_exchange):
    amount = amount / value_exchange
    amount = round(amount, 2)
    return amount

#Funtion to change between currencies that are not dollars
def exchange_other_other(amount, value_in, value_out):
    amount_in = exchange_other_dolar(amount, value_in)
    amount_out = exchange_dolar_other(amount_in, value_out)
    return amount_out

initial_message = """
Welcome to your favourite currency converter

Notes:
*You must choose your initial currency, the 
balance you have and the currency you want to 
change to.

*If you decide to withdraw your funds, you 
will be charged a '1%' fee

*Also, you should know that there is a minimum
and maximum withdrawal amount for each currency.

Currency available to exchange

1- CLP
2- ARS
3- USD
4- EUR
5- TRY
6- GBP
7- PEN
"""

#It start with a while loop to evaluate the reset variable.
#The cycle ends when this is false
while (reset == True):
    print(initial_message)
    print("Choose your initial currency.")
    initial_money = input("From the menu, choose a number form 1 to 7: ")
    #Evaluate if it is a valid answer
    if initial_money in available_operation:
        index_currency_in = int(initial_money) - 1  #Index that takes the coin in the first two declared lists
        currency_symbol_in = exchanges_symbols[index_currency_in]
        balance = input(f"\nHow much funds do you have: {currency_symbol_in} ")
        balance = float(balance)
        balance = round(balance,2)
        #Evaluate if that the balance is positive
        if balance >= 0:
            print("\nChoose the currency you want to change to.")
            final_money = input("From the menu, choose a number form 1 to 7: ")
            if final_money in available_operation:
                index_currency_out = int(final_money) - 1
                currency_symbol_out = exchanges_symbols[index_currency_out]
                #To bring in a variable the values that will be use to be able to carry out exchange operations
                initial_money_exchange = exchange_values[index_currency_in]
                final_money_exchange = exchange_values[index_currency_out]
                #Evaluate exchange cases
                if initial_money == final_money:
                    print(f"\n{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {balance}")
                    exchange_balance = balance
                elif initial_money == 3 and final_money != 3:
                    exchange_balance = exchange_dolar_other(balance, final_money_exchange)
                    print(f"\n{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {exchange_balance}") 
                elif initial_money != 3 and final_money == 3:
                    exchange_balance = exchange_other_dolar(balance, initial_money_exchange)
                    print(f"\n{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {exchange_balance}")
                else:
                    exchange_balance = exchange_other_other(balance, initial_money_exchange, final_money_exchange)
                    print(f"\n{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {exchange_balance}")
                #The user decides to withdraw or not
                answer = input("\nDo you want to withdraw the funds?(y/n): ")
                if answer in available_answers[0:4]:
                    min_withdraw = exchange_dolar_other(min_amount, final_money_exchange)
                    min_withdraw = int(min_amount)
                    max_witdhdraw = exchange_dolar_other(max_amount, final_money_exchange)
                    max_witdhdraw = int(max_amount)
                    print(f"The minimum amount must be between {currency_symbol_out} {min_withdraw} and {currency_symbol_out} {max_witdhdraw}")
                    #If the amount is between the minimum and maximum values, the witdhawal proceeds
                    if min_amount <= exchange_balance and exchange_balance <= max_amount:
                        commision = 0.01*exchange_balance
                        commision = round(commision, 2)
                        withdrawn_fund = exchange_balance - commision
                        withdrawn_fund = round(withdrawn_fund, 2)
                        print(f"\nCommision: {currency_symbol_out} {commision}")
                        print(f"Withdrawn fund: {currency_symbol_out} {withdrawn_fund}")
                        print("\nCongratulations. Successful operation ..!!")
                        #The return to the main menu is evalued
                        reset_init = input("\nDo you want to perfom another operation? (y/n): ")
                        reset = reset_menu(reset_init)
                    else:
                        print("Insufficient fund. Operation rejected ..!!")
                        #The return to the main menu is evalued
                        reset_init = input("\nDo you want to perfom another operation? (y/n): ")
                        reset = reset_menu(reset_init)
                elif answer in available_answers[4:8]:
                    print("\nOk.!!!")
                    reset_init = input("\nDo you want to return to the main menu? (y/n): ")
                    reset = reset_menu(reset_init)
                else:
                    reset = False
                    custom_message("Sorry. Incorrect. Invalid answer.!!!")
            else:
                reset = False
                custom_message("Sorry. Incorrect number chosen .!!!")
        else:
            reset = False
            custom_message("\nSorry. Incorrect amount of funds.!!!")
    else:
        reset = False
        custom_message("Sorry. Incorrect number chosen .!!!")