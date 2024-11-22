# Objective: The aim of this assignment is to reinforce the understanding of
#encapsulation in Python, focusing on the use of private attributes and getters and setters.

# Problem Statement: You are required to build a Personal Budget Management application.
#The application will manage budget categories like food, entertainment, utilities, etc.,
#ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for 
#category name and allocated budget. - Initialize these attributes in the constructor.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name
#and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

#Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the
#budget accordingly. - Validate the expense amount before making deductions from the budget.

#Task 4: Display Budget Details Create a method to display the details of a budget category, including
#the name, allocated budget, and remaining budget after expenses.


#Task 1
class BudgetCategory:                                                                                                                            #Defining a class named BudgetCategory
    def __init__(self, category, budget):                                                                                                        #initializing class 
        self.__category = category                                                                                                               #private attribute
        self.__budget = budget                                                                                                                   #private attribute
        ###Task3###
        self.expenses = []                                                                                                                       #set up a list to track expenses

    #Task 2
    def set_category(self, new_category):                                                                                                        #setter for category attribute
        self.__category = new_category 

    def get_category(self):                                                                                                                      #getter for category attribute
        return self.__category
    
    def get_budget(self):                                                                                                                        #getter for budget
        return self.__budget
    
    def set_budget(self, new_budget):                                                                                                            #setter for budget
        if new_budget >= 0:                                                                                                                      #if block to make sure the budget is a number at or above 0
            self.__budget = new_budget
        else:                                                                                                                                    #else block letting the user know the budget must be positive or equal to 0
            print("Budget must be 0 or above, it can't be negatvie.")    


    #Task 3   
    def budget_expense(self, expense):                                                                                                          #method for adding expenses to the budget
        if self.get_budget() >= expense:                                                                                                        #if block to check and see if the expense will make the budget go negatvie
            self.expenses.append(expense)                                                                                                       #appending the expense to the expenses list
            self.set_budget(self.get_budget() - expense)                                                                                        #taking the expenses out of the budget
            print(f"{expense} has been taken out of the budget. The remaining budget is {self.get_budget()}.")                                  #letting the user know the expense has been taken out of the budget
        else:
            print("This expense has not been recorded because this will cause the buget to go negatvie.")                                       #else block letting the user know the expense will cause the budget to go negatvie                             
           

    #Task 4
    def display_budget_details(self):                                                                                                           #method to display the details of the budget
        print(f"Budget: {self.get_category()}\nAllocated to budget: {sum(self.expenses) + self.get_budget()}\nAllocated from budget: {sum(self.expenses)}\nRemaining Budget: {self.get_budget()}") 
                 
 

budgets = {}

def add_budget(budget_name, category, budget):                                                                                                 #function to add a buget to the buget class and budgets list
    budget_name2 = budget_name
    budget_name = BudgetCategory(category, budget)
    budgets[budget_name2] = budget_name
    


while True:                                                                                                                                   #while loop to cycle through some options for the user
    print("Welcome to the budget managments system.\n")                                                                                       #welcome statement
    print("1.Add Budget\n2.Alter Budget\n3.Alter category\n4.Add Expense\n5.View Budget Details\n6.Exit")                                     #printing the options for the user
    user_cho = input("Select the function you'd like to perform (1-6): ")                                                                     #getting the user's option choice
 
    if user_cho == "1":                                                                                                                       #if block determining the user choice
        try:                                                                                                                                  #try block for error handling
            budg_name = input("Enter the name of this budget: ")                                                                              #getting user inputs
            cat = input("Enter the category for this budget: ")
            budg_value = float(input("Enter the amount being allocated to the budget (00.00): "))
            add_budget(budg_name, cat, budg_value)                                                                                            #calling function to add budget
        except ValueError:                                                                                                                    #except block for ValueError
            print("One of the inputs wasnt recognized. The budget must be a number.")                                                         #informing the user an input was not valid

    elif user_cho == "2":                                                                                                                     #elif block determining the user choice
        print("These are the current budgets:")                                                                                               #print statement
        for budget in budgets:                                                                                                                #for loop running through the budgets list
            print(budget)                                                                                                                     #printing off the budgets in list for the user
        budg_name = input("Enter the name of the budget you would like to alter: ")                                                           #gaining user inputs  
        new_budget = float(input("Enter the new budget please: "))                                                                            
        if budg_name in budgets:                                                                                                              #if block checking the user input against the budgets list
            budgets[budg_name].set_budget(new_budget)                                                                                         #setting the new budget
            print(f"The budget for {budg_name} has been changed to {new_budget}")                                                             #print statement informing the user the budget has been changed
        else:                                                                                                                                 #else block in case the budget isnt found in the budgets list
            print("Budget not found.")    

    elif user_cho =="3":                                                                                                                      #elif block determining the user choice
        print("These are the current budgets:")                                                                                               #print statement
        for budget in budgets:                                                                                                                #for loop running through the budgets list
            print(budget)                                                                                                                     #printing off the budgets in list for the user
        budg_name = input("Enter the name of the budget you would like to alter: ")                                                           #getting user inputs
        new_category = input("Enter the new category please: ")  
        if budg_name in budgets:                                                                                                              #if block checking the user input against the budgets list
            budgets[budg_name].set_category(new_category)                                                                                     #updating the category
        else:                                                                                                                                 #else block informing the user the budget couldnt be found
            print("Budget not found.")

    elif user_cho == "4":                                                                                                                     #elif block determining the user choice
        print("These are the current budgets:")                                                                                               #print statement
        for budget in budgets:                                                                                                                #for loop running through the budgets list
            print(budget)                                                                                                                     #printing off the budgets in list for the user
        budg_name = input("Enter the name of the budget you would like to add an expense to: ")                                               #getting user inputs
        expense_amount = float(input("Enter the amount of the expense (00.00): "))                                                       
        if budg_name in budgets:                                                                                                              #if block checking the user input against the budgets li
            budgets[budg_name].budget_expense(expense_amount)                                                                                 #adding the expense to the selected budget   
        else:                                                                                                                                 #else block informing the user the budget couldnt be found
            print("Budget not found.")    

    elif user_cho == "5":                                                                                                                     #elif block determining the user choice
        print("These are the current budgets:")                                                                                               #print statement
        for budget in budgets:                                                                                                                #for loop running through the budgets list
            print(budget)                                                                                                                     #printing off the budgets in list for the user
        budg_name = input("Enter the name of the budget you would like to see details for: ")                                                 #getting user inputs
        if budg_name in budgets:                                                                                                              #if block checking the user input against the budgets li
            budgets[budg_name].display_budget_details()                                                                                       #displaying the details of the selected budget
        else:                                                                                                                                 #else block informing the user the budget couldnt be found
            print("Budget not found")    
            
    elif user_cho == "6":                                                                                                                     #elif block determining the user choice
        break                                                                                                                                 #break statement ending the loop

    else:                                                                                                                                     #else statemetn informing the user their input was not recognized
        print("Input not recognized. Please enter a number 1-6 as your selection.")
