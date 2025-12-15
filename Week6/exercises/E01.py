class BankAccount():
    interest_rate = 30
    
    def __init__(self, account_num, account_type, customer_id, balance, created_date):
        self.account_num = account_num
        self.account_type = account_type
        self.customer_id = customer_id
        self.balance = balance
        self.created_date = created_date

    def deposit(self, amount):
        if amount is None or amount < 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount is None or amount < 0 or amount > self.balance:
            return False

        self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + self.interest_rate / 100

    def __str__(self):
        print(f"Account {self.account_num} {self.account_type}: ${self.balance}",
              f"Created: {self.created_date}")

bankAccount1 = BankAccount('0001', 'Savings', '1111', 20000, '01/01/2024')
bankAccount2 = BankAccount('0002', 'Current', '1112', 5000, '03/11/2000')

# some transactions
bankAccount1.__str__()
print()
bankAccount2.__str__()
print()
bankAccount1.deposit(5000)
bankAccount1.add_interest()
bankAccount2.withdraw(200)
print()
bankAccount1.__str__()
print()
bankAccount1.__str__()
