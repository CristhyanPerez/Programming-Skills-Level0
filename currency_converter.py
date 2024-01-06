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
4- TRY
5- GBP
"""

print(initial_message)
print("Choose your initial currency.")
initial_money = input("From the menu, choose a number form 1 to 5: ")
balance = input("\nHow much funds do you have: ")
balance = int(balance)
print("\nChoose the currency you want to change to.")
final_money = input("From the menu, choose a number form 1 to 5: ")