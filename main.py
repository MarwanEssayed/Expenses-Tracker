file = "expenses.txt"

def Welcome():
    print("Personal Expenses Tracker")
    print("-------------------------")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expenses")
    print("5. Exit")
    print("-------------------------")
    print()
    
def load_expenses():
    expenses = []
    
    try:
        with open(file,"r") as f:
            for line in f:
                category, amount = line.strip().split(",")
                expenses.append({"category":category, "amount":float(amount)})
    except FileNotFoundError:
        print("File does not exist")
    except Exception as e:
        print(e)
    return expenses
        
def save_expenses(expenses):
    with open(file,"w") as f:
        for e in expenses:
            f.write(f"{e["category"]},{e["amount"]}\n")   

def add_expense(expenses):
    try:
        category = input("Enter Your Category: ")
        amount = float(input("Enter The Amount: "))
        expenses.append({"category":category , "amount":amount})
        save_expenses(expenses)
        print("Expense Added Successfully")
    except ValueError:
        print("Invalid Amount Input")
    except Exception as e:
        print(e)
        
def view_expense(expenses):
    print("\nExpenses: ")
    i = 1
    for e in expenses:
        print(f"{i}. {e["category"]} = {e["amount"]}$")
        i +=1
    print()
    
def total_expense(expenses):
    total = 0
    for e in expenses:
        total += e["amount"]
    print(f"Your Total Expenditure is: {total}$")
    
def remove_expense(expenses):
    if not expenses:
        print("\n There are no expenses to remove.")
        return
        
    view_expense(expenses)
    try:
        number = int(input("Enter Your Number: "))
        if number >= 1 and number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"You Removed: {removed["category"]} - {removed["amount"]}$")
        else:
            print("Invalid Number\n")
    except ValueError:
        print("Enter Valid Number")
        
def main():
   
    expenses = load_expenses()
    
    while True:
        Welcome()
        
        choice = input("Choose: ")
        
        if choice == "1":
            add_expense(expenses)
        
        elif choice == "2":
            view_expense(expenses)
        
        elif choice == "3":
            total_expense(expenses)
        
        elif choice == "4":
            remove_expense(expenses)
        
        elif choice == "5":
            print("Thank You For Using Our Application")
            return
        

main()