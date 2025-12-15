class Account():
    interest_rate = 0.3

    def __init__(self, account_num, account_type, balance, created_date):
        self.account_num = account_num
        self.account_type = account_type
        self.balance = balance
        self.created_date = created_date

class Customer():
    def __init__(self, customer_id, name, address, email):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email

        self.accounts = []    

    def add_bank_account(self, account_num, account_type, balance, created_date):
        try:
            new_Account = Account(account_num, account_type, balance, created_date)
            self.accounts.append(new_Account)
            return True
        except Exception as e:
            print(f"Unable to add account due to: {e}")
            return False

    def remove_bank_account(self, account_num_to_remove):
        try:
            for account in self.accounts:
                if account.account_num == account_num_to_remove:
                    self.accounts.remove(account)
                    return True
            print(f"Account not found")
            return False
        except Exception as e:
            print(f"Unable to remove account due to: {e}")
            return False

    def deposit(self, account_num, amount):
        try:
            for account in self.accounts:
                if account.account_num == account_num:
                    account.balance += amount
                    return True
            print("Account not found")
            return False
        except Exeption as e:
            print(f"Unable to deposit due to: {e}")
            return False

    def withdraw(self, account_num, amount):
        try:
            for account in self.accounts:
                if account.account_num == account_num:
                    account.balance -= amount
                    return True
            print("Account not found")
            return False
        except Exeption as e:
            print(f"Unable to withdraw due to: {e}")
            return False

    def get_bank_account(self, account_num):
        for account in self.accounts:
            if account.account_num == account_num:
                return f"Account {account.account_num} ({account.account_type} | {account.created_date}) - Balance: {account.balance}"

        print("Account not found")
        return None

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        return f"The total balance is: {total_balance}"

    def add_interest_to_accounts(self):
        for account in self.accounts:
            account.balance += account.balance * account.interest_rate

    def get_customer_info(self):
        return f"{self.customer_id}, Name: {self.name}, Address: {self.address}, Email: {self.email}"
        
    def __str__(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        return self.customer_id + ": Total Balance = " + str(total_balance)

customer_init = Customer('0001', 'Michelle Burman', '23 Duck Street', 'mike@email.eu')
print(customer_init)
print(customer_init.add_bank_account(1111, 'Current', 5000 ,'2025-01-01'))
print(customer_init.add_bank_account(2222, 'Savings', 50000 ,'2025-02-02'))
print(customer_init.get_bank_account(1111))
print()
#print(customer_init.remove_bank_account(1111))
print()
print(customer_init.deposit(1111, -2000))
print(customer_init.get_bank_account(1111))
print()
print(customer_init.withdraw(1111, 250))
print(customer_init.get_bank_account(1111))
print(customer_init.get_bank_account(2222))
print()
print(customer_init.get_total_balance())
print()
print(customer_init.add_interest_to_accounts())
print(customer_init.get_bank_account(1111))
print(customer_init.get_bank_account(2222))
print()
print(customer_init.get_customer_info())
print(customer_init)
