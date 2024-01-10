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
    max_expense = max(list_expenses)
    return list_expenses[0], list_expenses[1], list_expenses[2], list_expenses[3], list_expenses[4], max_expense

#Funtion to print a summary and evaluate the total expense
def summary_final(income, medical, household, leisure, saving, education):
    total_expense = medical + household + leisure + saving + education
    summary = f"""
        *************************  Summary  ***************************
        
        Total income:           $ {income}
        
        Expenses by category:
        * Medical expenses      $ {medical}
        * Household expenses    $ {household}
        * Leisure               $ {leisure}
        * Savings               $ {saving}
        * Education             $ {education}

        Total expenses:         $ {total_expense}
        
        ***************************************************************
        """
        print(summary)

#Final messages for the user
message_01 = """
Congratulations! 
You have shown great financial discipline by 
spending less than you earn. 

Remember what Bill said: 'It is well known that
the surest way to double your money is to double
it and put it in your pocket.'
"""

message_02 = """
Oh no! You are spending more money than you earn. Don't worry,
here I have some tips to improve your financial life.

* Create a monthly budget to control your expenses.
* Reduce non-essential expenses and look for cheaper alternatives.
* Increase your income with additional jobs or side projects.
* Prioritize paying debts, especially those with high interest.
* Save regularly, even if it's a small amount.

Warren Buffett advices: 'Don't save what you have left after
spending; spend what you have left after saving.'
This approach can be a game changer in your financial life.
"""

message_03 = """
Warning.! Spending the same as you earn be risky, since it
does not allow you to save for emergencies.

Remember the words of Sergey Brin: 'It's not enough to have
a good idea; you have to act on it.' 
Apply this to your finances:  look for ways to reduce expenses
or increase income for a more secure future.
"""
