import json

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

def add_expense():
    amount = input("Amount: ")
    category = input("Category: ")
    description = input("Description: ")
    date = input("Date: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense saved successfully!")

def view_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No expenses found.")
        return

    if not expenses:
        print("No expenses found.")
        return

    print("\n==============================")
    print("        Your Expenses")
    print("==============================")

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense #{index}")
        print(f"Category: {expense['category']}")
        print(f"Amount: {expense['amount']}")
        print(f"Description: {expense['description']}")
        print(f"Date: {expense['date']}")
        print("------------------------------")
        
   
def main():
    is_on = True
    while is_on:
        
        user_answer = initial_display()
        
        if user_answer == "1":
            add_expense()
        elif user_answer == "2":
            view_expenses()
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
    
