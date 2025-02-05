class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

# Example usage
account = BankAccount("Alice", 100)
account.deposit(50)  # Deposited 50. New balance: 150
account.withdraw(30)  # Withdrew 30. New balance: 120
account.withdraw(200)  # Insufficient funds.
account.deposit(-20)  # Deposit amount must be positive.
account.withdraw(-10)  # Withdrawal amount must be positive.
