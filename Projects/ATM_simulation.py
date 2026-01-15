# ATM Simulation

balance = 5000  # Initial balance

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: $"))
        balance += amount
        print(f"Deposited ${amount}. New balance: ${balance}")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
