import random

biscuits = ['Monte Carlo'] * 7 + ['Shortbread Cream'] * 7 + ['Delta Cream'] * 6 + ['Orange Slice'] * 6 + ['Kingston'] * 5

print("\nASSORTED CREAMS\n")
print("There are ", len(biscuits), "biscuits in the pack.")
print("\n", biscuits, "\n")
more = input("\nWould you like a biscuit (Y/N): ")
while more != "N":
    choice = random.randint(0, len(biscuits) - 1)
    print("Your biscuit is: ", biscuits[choice])
    del biscuits[choice]
    add = input("\nWould you like to add biscuits (Y/N): ")
    if add == "Y":
        newBiscuit = input("\nEnter biscuit name: ")
        newBiscuitAmount = int(input("\nEnter biscuit amount: "))
        newBiscuitList = [newBiscuit] * newBiscuitAmount
        biscuits.extend(newBiscuitList)
    more = input ("\nWould you like a biscuit (Y/N): ")
print("\nThere are ", len(biscuits), "bicuits left.")
print("\n", biscuits, "\n")
