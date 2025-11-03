# range(10) => [0, 1, 2, ..., 9] <= 10 items
for i in range(10):
    print("Hello")

fruits = ['apple', 'orange', 'pear']
for fruit in fruits:
    print(fruit)

# len(fruits) => 3
# range(len(fruits)) => range(3) => [0, 1, 2]
for i in range(len(fruits)):
    print(fruits[i])
# the for loop becomes
# for i in [0, 1, 2] <= the index list

# stock, prices and fruits are parallel list
# the related items has the same index
# using the three lists as example:
# - apple stock is 10 and price is 0.8
# - orange stock is 12 and price is 0.9
# - pear stock is 8 and price is 1.1
stock = [19, 12, 8]
prices = [0.8, 0.9, 1.1]
fruits = ['apple', 'orange', 'pear']
for i in range(len(fruits)):
    print(f"{fruits[i]} ${prices[i]} stock:{stock[i]}")

for i in range(len(prices)):
    new_price = prices[i] * 1.1
    # round off to two dec places using round()
    new_price = round(new_price, 2)
    #update the price to a new price
    prices[i] = new_price

for i in range(len(fruits)):
    print(f"{fruits[i]} ${prices[i]} stock:{stock[i]}")
