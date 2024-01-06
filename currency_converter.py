exchange_values = [892.86, 811.20, 1.00, 0.91, 29.82, 0.79, 3.69]

def exchange_dolar_other(amount, value_exchange):
    amount = amount * value_exchange
    amount = round(amount, 2)
    return amount

def exchange_other_dolar(amount, value_exchange):
    amount = amount / value_exchange
    amount = round(amount, 2)
    return amount

def exchange_other_other(amount, value_in, value_out):
    amount_in = exchange_other_dolar(amount, value_in)
    amount_out = exchange_dolar_other(amount_in, value_out)
    return amount_out

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
    elif number_money == "7":
        symbol = "PEN"
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
7- PEN
"""

print(initial_message)
print("Choose your initial currency.")
initial_money = input("From the menu, choose a number form 1 to 7: ")
if initial_money == "1" or initial_money == "2" or initial_money == "3" or initial_money == "4" or initial_money == "5" or initial_money == "6" or initial_money == "7":
    currency_symbol_in = symbol_money(initial_money)
    balance = input(f"\nHow much funds do you have: {currency_symbol_in} ")
    balance = float(balance)
    balance = round(balance,2)
    if balance >= 0:
        print("\nChoose the currency you want to change to.")
        final_money = input("From the menu, choose a number form 1 to 7: ")
        currency_symbol_out = symbol_money(final_money)
        if final_money == "1" or final_money == "2" or final_money == "3" or final_money == "4" or final_money == "5" or final_money == "6" or final_money == "7":
            initial_money = int(initial_money)
            final_money = int(final_money)
            initial_money_exchange = exchange_values[initial_money - 1]
            final_money_exchange = exchange_values[final_money - 1]
            if initial_money == final_money:
                print(f"{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {balance}")
            elif initial_money == 3 and final_money != 3:
                exchange_balance = exchange_dolar_other(balance, final_money_exchange)
                print(f"{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {exchange_balance}") 
            elif initial_money != 3 and final_money == 3:
                exchange_balance = exchange_other_dolar(balance, initial_money_exchange)
                print(f"{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {exchange_balance}")
            else:
                exchange_balance = exchange_other_other(balance, initial_money_exchange, final_money_exchange)
                print(f"{currency_symbol_in} {balance} is equivalent to {currency_symbol_out} {exchange_balance}")
        else:
            print("\nSorry. Incorrect number chosen.!!!")
            print("Come back soon. Thanks")
    else:
        print("\nSorry. Incorrect amount of funds.!!!")
        print("Come back soon. Thanks")
else:
    print("\nSorry. Incorrect number chosen.!!!")
    print("Come back soon. Thanks")
