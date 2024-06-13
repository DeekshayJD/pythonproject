class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Protected attribute
        self.balance = balance  # Protected attribute

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


# Create an instance of BankAccount
account1 = BankAccount("123456789", 1000)

# Attempt to access protected attributes directly
print(account1.account_number)  # Output: 123456789
print(account1.balance)         # Output: 1000


#Try to deposit and withdraw
account1.deposit(500)
print(account1.get_balance())    # Output: 1500

account1.withdraw(2000)          # Output: Insufficient funds
print(account1.get_balance())    # Output: 1500

