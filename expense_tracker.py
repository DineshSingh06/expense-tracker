def add_expense():
    category = input("Enter category: ")
    while True:
        try:
            amount = int(input("Enter amount: "))

            if amount<=0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Enter a valid amount")

    with open("expenses.txt","a")as f:
        f.write(f"{category},{amount}\n")
    print("Expense added successfully!")

def view_expenses():
    with open("expenses.txt")as f:
        expenses = f.readlines()
    
    if not expenses:
        print("\nNo expenses recorded.")
        return  
    
    print("\n=====All Expenses=====")
    for line in expenses:
        category, amount = line.strip().split(",")
        print(f"Category: {category}")
        print(f"Amount: ₹{amount}\n")
        

def view_total():
    total = 0
    with open("expenses.txt")as f:
        expenses = f.readlines()
    if not expenses:
        print("\nNo expenses recorded.")
        return
    for line in expenses:
        category, amount = line.strip().split(",")
        total += int(amount)
    print(f"Total Expense = ₹{total}")

while True:
    print("=========================")
    print("     Expense Tracker     ")
    print("=========================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")