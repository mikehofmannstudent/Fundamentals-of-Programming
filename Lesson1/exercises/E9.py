numAdult = int(input("Enter the number of adults: "))
numChild = int(input("Enter the number of children: "))
animalShow = input("Are you seeing the animal show? (yes, no): ")
isFriend = input("Are you a 'friend of Zoo'? (yes, no): ")

cost = numAdult * 15 + numChild * 10

if(animalShow == "yes"):
    cost += numAdult * 5 + numChild * 5

if(cost > 150 or isFriend == "yes"):
    cost *= 0.9

if(cost > 100):
    print(f"Your total is {cost}, and everyone will be recieving free sunshades.")
else:
    print(f"Your total is {cost}.")
    