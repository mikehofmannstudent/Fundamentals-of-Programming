class BankAccount():
    # class variable
    interest_rate = 0.3

    # constructor
    def __init__(self, name , number, balance):
        self.name = name
        self.number = number
        self.balance = balance

accounts = []
bank = BankAccount('Everyday', '007', 2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C', '008', 3000)
accounts.append(bank)
bank = BankAccount('Term Deposit', '009', 20000)
accounts.append(bank)
total = 0

for i in range(len(accounts)):
    print("Name: ", accounts[i].name,
          "\tNumber: ", accounts[i].number,
          "\tBalance: ", accounts[i].balance)
    total = total + accounts[i].balance
print("Total: ", total)
