import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
        
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
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
    
    if not amount.isdigit():
        print("Please enter a valid amount.")
        return

    if int(amount) == 0:
        print("Amount must be greater than zero.")
        return
    
    category = input("Category: ")
    description = input("Description: ")
    date = input("Date: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses = load_expenses()

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense saved successfully!")

def view_expenses():
    
    expenses = load_expenses()
    
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
        
def delete_expense():
    
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['amount']} - "
            f"{expense['description']}"
        )

    choice = input("Choose expense to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(expenses):
        print("Expense not found.")
        return

    expenses.pop(choice - 1)

    save_expenses(expenses)

    print("Expense deleted successfully!")

def show_total():
    
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    print(f"Total Expenses: {total}")
   