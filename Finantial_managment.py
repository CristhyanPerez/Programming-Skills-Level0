available_options = ["1", "2", "3", "4", "5"]
categories = ["Medical expenses", "Household expenses", "Leisure", "Savings", "Education"]
expenses_categories = [0, 0, 0, 0, 0]

#Funtion to validate if the amount is positive
def validate_amount(sentence):
    #Declare the start variable
    verify = False
    number = float(input(sentence))
    number = round(number, 2)
    #If number is positive, skip the loop
    if number > 0:      
        verify = True
    while verify == False:
        print("\nThe amount placed is incorrect.")
        print("Only positive values are accepted. Retry..!!\n")
        number = float(input(sentence))
        number = round(number, 2)
        #If number is negative, go back to the loop
        if number > 0:
            verify = True
        else:
            verify = False
    return number

#Function to validate the category chosen
def validate_category(list_options):
    #Declare the start variable
    verify = False
    category = input("Category to which the expense belong (1-5): ")
    #Verify if the chosen number is within the available list
    if category in list_options:
        verify = True
    while verify == False:
        print("\nIncorrect category number chosen.")
        print("Only values from 1 to 5 ..!!\n")
        category = input("Category to which the expense belong (1-5): ")
        #If the number of category is incorrect, go back to the loop
        if category in list_options:
            verify = True
        else:
            verify = False
    category = int(category)
    return category

#Function to ask about the expense and the category. Return the list with update expenses by category
def category_expense(list_options, list_categories, list_expenses):
    continue_loop = True
    #The loop continues until the user decides not to add more expenses
    while continue_loop == True:
        amount_in = validate_amount("Enter the expense incurred: $ ")
        chosen_category = validate_category(list_options)
        category = list_categories[chosen_category - 1]
        print(f"\nThe expense entered is {amount_in} and corresponds to the '{category}' category\n")
        list_expenses[chosen_category - 1] = list_expenses[chosen_category - 1] + amount_in
        continue_question = True
        #Evaluate that the answer is only 'y' or 'n'. Id it's another ask again
        while continue_question == True:
            answer = input("Do you want to add another expense?(y/n): ")
            if answer == "y" or answer == "yes":
                continue_loop = True
                continue_question = False
                print()
            elif answer == "n" or answer == "no":
                continue_loop = False
                continue_question = False
                print("Ok. Great.!\n")
            else :
                print("Wrong answer ...!!!")
                print("I will ask again\n")
                continue_question = True
    return list_expenses[0], list_expenses[1], list_expenses[2], list_expenses[3], list_expenses[4]

#Funtion to print a summary and evaluate the total expense




a, b, c, d, e = category_expense(available_options, categories, expenses_categories)

print(a)
print(b)
print(c)
print(d)
print(e)