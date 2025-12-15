class BankAccount():
    # class variable
    interest_rate = 0.3

    # constructor
    def __init__(self, name , number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def add_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

def balances():
    total = 0
    for i in range(len(accounts)):
        print("Name: ", accounts[i].number,
              "\tNumber: ", accounts[i].number,
              "\tBalance: ", accounts[i].balance)
        total = total + accounts[i].balance
    print("Total: ", total)
    
accounts = []
bank = BankAccount('Everyday', '007', 2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C', '008', 3000)
accounts.append(bank)
bank = BankAccount('Term Deposit', '009', 20000)
accounts.append(bank)
balances()



print("\nDoing some transactions...\n")
accounts[0].deposit(100)
accounts[1].withdraw(500)
accounts[2].add_interest()
balances()
