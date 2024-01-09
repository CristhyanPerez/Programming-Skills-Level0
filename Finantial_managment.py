available_options = ["1", "2", "3", "4", "5"]

#Create a dictionary where the key will be category and the value will be the amount spent
categories = {
    "Medical expenses"  : 0,
    "Houshold expenses" : 0,
    "Leisure"           : 0,
    "Savings"           : 0,
    "Education"         : 0
}

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

#Function to ask about the expense and the category
def category_expense(list_options, dictionary_categories):
    list_key = list(dictionary_categories.keys())
    amount_in = validate_amount("Enter the expense incurred: $ ")
    chosen_category = validate_category(list_options)
    index_category = chosen_category - 1
    category = list_key[index_category]
    print(f"\nThe expense entered is {amount_in} and corresponds to the {category} category")

category_expense(available_options, categories)    