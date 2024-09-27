class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance}")

        else:
            print("Invalid deposit amount. Please try again.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance}")

        else:
            print("Invalid withdrawal amount. Please try again.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

def main():
    accounts = {}

    def create_account():
        account_number = input("Enter account number. ")
        if account_number in accounts:
            print("Account number already exists. Please try again.")

        else:
            owner = input("Enter account owner's name. ")
            accounts[account_number] = Account(account_number, owner)
            print(f"Account created successfully for {owner}")

    def access_account():
        account_number = input("Enter account number. ")
        if account_number in accounts:
            account = accounts[account_number]
            print(f"Welcome, {account.owner}")

            while True:
                print("\n1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")

                choice = input("Choose an option: ")

                if choice == "1":
                    account.check_balance()

                elif choice == "2":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif choice == "4":
                    print("Logging out...")
                    break

                else:
                    print("Invalid option. Please try again.")

        else:
            print("Account not found.")

    while True:
        print("\n--- Welcome To The Bank ---")
        print("\n1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            access_account()

        elif choice == "3":
            print("Thank You for Using The Bank!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()