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
        print("Add Expense selected.")

    elif choice == "2":
        print("View Expenses selected.")

    elif choice == "3":
        print("View Total Expense selected.")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")