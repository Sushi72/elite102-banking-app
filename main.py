from accounts import create_account, deposit, withdraw, check_balance, list_accounts

def menu():
    print("==== Welcome to Bank of Sushi! ====")
    print("1. Create Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Check Your Account Balance")
    print("5. List of Accounts")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Select one of The options above: ")

        if choice == "1":
            name = input("Enter account name: ")
            deposit_amount = float(input("Enter initial deposit: "))
            create_account(name, deposit_amount)

        elif choice == "2":
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter deposit amount: "))
            deposit(account_id, amount)

        elif choice == "3":
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account_id, amount)

        elif choice == "4":
            check_balance(int(input("Enter account ID: ")))

        elif choice == "5":
            list_accounts()

        elif choice == "6":
            print("Thank you for using Bank of Sushi!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()


