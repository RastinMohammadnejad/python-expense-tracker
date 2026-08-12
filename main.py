def initial_display():
    user_option = input("""
==============================
    Python Expense Tracker
=============================
    1. Add Expense
    2. View Expenses
    3. Delete Expense
    4. Show Total
    5. Exit
==============================
    Choose an option:""")
    return user_option
    
def main():
    is_on = True
    while is_on:
        
        user_answer = initial_display()
        
        if user_answer == "1":
            print("Add Expense")
        elif user_answer == "2":
            print("View Expenses")
        elif user_answer == "3":
            print("Delete Expense")
        elif user_answer == "4":
            print("Show Total")
        elif user_answer == "5":
            print("Goodbye")
            is_on = False
        else:
            print("Please choose a valid option!")
    
        
    
     
if __name__ == "__main__":
    main()
    
