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
        print(f"You selected: {user_answer}")
    
     
if __name__ == "__main__":
    main()