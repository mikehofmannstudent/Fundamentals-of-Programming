gender = input("Enter your gender (M-Male, F-Female): ")
amountSpent = int(input("Enter your aount spent: "))
freeGift = ""

if(gender == "M"):
    if(amountSpent >= 100):
        freeGift = "a shaver"
    else:
        freeGift = "nothing"
if(gender == "F"):
    if(amountSpent >= 100):
        freeGift = "hand cream"
    else:
        freeGift = "nothing"

print(f"Your free gift will be {freeGift}")