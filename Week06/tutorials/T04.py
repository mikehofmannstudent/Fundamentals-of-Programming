class BankAccount():
    # class variable
    interest_rate = 0.3

    # constructor
    def __init__(self, name , number, balance):
        self.name = name
        self.number = number
        self.balance = balance

# create a BankAccount object
bank = BankAccount('Everyday', '007', 2000)
print("Name: ", bank.name,
      "\tNumber: ", bank.number,
      "\tBalance: ", bank.balance)
