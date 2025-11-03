cost = int(input("Enter purchase amount: "))
bank = input("Enter bank name (DBS, OCBC, other): ")

if(bank == "DBS" and cost > 200):
    cost = cost * 0.9
elif(bank == "OCBC" and cost > 200):
    cost = cost * 0.85
elif(bank == "other" and cost > 200):
    cost = cost * 0.95

print(f"Your total cost will be ${cost}.")
    