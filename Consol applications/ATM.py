class ATM:
    def __init__(self, filename):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.accounts = {}
                for line in file:
                    account_number, pin, balance = line.strip().split(",")
                    self.accounts[account_number] = {"pin": pin, "balance": float(balance)}
        except FileNotFoundError:
            print("Account data file not found.")

    def save_data(self):
        with open(self.filename, "w") as file:
            for account_number, account_info in self.accounts.items():
                file.write(f"{account_number},{account_info['pin']},{account_info['balance']}\n")

    def authenticate(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            return True
        else:
            return False

    def check_balance(self, account_number):
        return self.accounts[account_number]["balance"]

    def deposit(self, account_number, amount):
        self.accounts[account_number]["balance"] += amount
        self.save_data()
        return self.accounts[account_number]["balance"]

    def withdraw(self, account_number, amount):
        if self.accounts[account_number]["balance"] >= amount:
            self.accounts[account_number]["balance"] -= amount
            self.save_data()
            return self.accounts[account_number]["balance"]
        else:
            return "Insufficient funds"


def main():
    atm = ATM("account_data.txt")

    while True:
        print("\nWelcome to the ATM")
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if atm.authenticate(account_number, pin):
            while True:
                print("\nChoose an option:")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    balance = atm.check_balance(account_number)
                    print("Your balance is:", balance)
                elif choice == "2":
                    amount = float(input("Enter the amount to deposit: "))
                    balance = atm.deposit(account_number, amount)
                    print("Deposit successful. Your new balance is:", balance)
                elif choice == "3":
                    amount = float(input("Enter the amount to withdraw: "))
                    result = atm.withdraw(account_number, amount)
                    if isinstance(result, str):
                        print(result)
                    else:
                        print("Withdrawal successful. Your new balance is:", result)
                elif choice == "4":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid account number or PIN. Please try again.")


if __name__ == "__main__":
    main()
