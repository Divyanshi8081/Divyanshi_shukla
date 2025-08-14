import random
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self.generate_account_number()
        self.account_holder = account_holder
        self.balance = balance

    def generate_account_number(self):
        return random.randint(10**15, (10**16) - 1)  # 16-digit number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")
class SavingAccount(BankAccount):
    interest_rate = 4  
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied at {self.interest_rate}% rate.")
class CurrentAccount(BankAccount):
    overdraft_limit = 50000 

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully (Overdraft allowed).")
        else:
            print(f"Withdrawal exceeds overdraft limit of ₹{self.overdraft_limit}.")

def main():
    account_type = input("Enter account type (saving/current): ").strip().lower()
    name = input("Enter account holder name: ").strip()
    balance = float(input("Enter initial balance: "))

    if account_type == "saving":
        account = SavingAccount(name, balance)
        print("\nYour account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Interest Rate (Bank Fixed): {account.interest_rate}%")
    elif account_type == "current":
        account = CurrentAccount(name, balance)
        print("\nYour account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Overdraft Limit (Bank Fixed): ₹{account.overdraft_limit}")
    else:
        print("Invalid account type. Exiting program.")
        return

    while True:
        print("\nChoose operation:")
        if account_type == "saving":
            print("1. Deposit\n2. Withdraw\n3. Display Balance\n4. Apply Interest\n5. Exit")
        else:
            print("1. Deposit\n2. Withdraw\n3. Display Balance\n5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)
        elif choice == "3":
            account.display_balance()
        elif choice == "4" and account_type == "saving":
            account.apply_interest()
        elif choice == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
