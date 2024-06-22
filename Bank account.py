class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Amount deposited: {amount:.2f}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Amount withdrawn: {amount:.2f}"

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Account Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", "2023-06-15", 1000.0)
    
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(1500))
    account.check_balance()
    account.customer_details()
