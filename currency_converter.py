def symbol_money(number_money):
    if number_money == "1":
        symbol = "CLP"
    elif number_money == "2":
        symbol = "ARS"
    elif number_money == "3":
        symbol = "USD"
    elif number_money == "4":
        symbol = "EUR"
    elif number_money == "5":
        symbol = "TRY"
    elif number_money == "6":
        symbol = "GBP"
    return symbol

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
"""

print(initial_message)
print("Choose your initial currency.")
initial_money = input("From the menu, choose a number form 1 to 5: ")
if initial_money == "1" or initial_money == "2" or initial_money == "3" or initial_money == "4" or initial_money == "5" or initial_money == "6":
    currency_symbol = symbol_money(initial_money)
    balance = input(f"\nHow much funds do you have: {currency_symbol} ")
    balance = float(balance)
    balance = round(balance,2)
    if balance >= 0:
        print("\nChoose the currency you want to change to.")
        final_money = input("From the menu, choose a number form 1 to 5: ")
        if final_money == "1" or final_money == "2" or final_money == "3" or final_money == "4" or final_money == "5" or initial_money == "6":
            print("hola")
        else:
            print("\nSorry. Incorrect number chosen.!!!")
            print("Come back soon. Thanks")
    else:
        print("\nSorry. Incorrect amount of funds.!!!")
        print("Come back soon. Thanks")
else:
    print("\nSorry. Incorrect number chosen.!!!")
    print("Come back soon. Thanks")

