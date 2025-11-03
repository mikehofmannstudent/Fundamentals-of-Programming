salery = int(input("Enter your yearly salery: "))
yearsEmployed = int(input("Enter the amount of years you have been employed: "))

conditionSalery = False
conditionYears = False

if(salery >= 50000):
    conditionSalery = True
else:
    print("You need to earn at least $50,000 per year.")
if(yearsEmployed >= 2):
    conditionYears = True
else:
    print("You need to be employed at your current job for at least 2 years.")

if(conditionSalery == True and conditionYears == True):
    print("You are qualified for a loan.")