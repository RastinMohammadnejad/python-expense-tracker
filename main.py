from expense_manager import *
 
def main():
    is_on = True
    while is_on:
        
        user_answer = initial_display()
        
        if user_answer == "1":
            add_expense()
            
        elif user_answer == "2":
            view_expenses()
            
        elif user_answer == "3":
            delete_expense()
            
        elif user_answer == "4":
            show_total()
            
        elif user_answer == "5":
            print("Goodbye")
            is_on = False
        else:
            print("Please choose a valid option!")
    
        
    
     
if __name__ == "__main__":
    main()
    
