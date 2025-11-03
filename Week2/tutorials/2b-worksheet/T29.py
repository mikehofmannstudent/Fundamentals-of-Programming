# converting a string to a list
# assume each item is seperated by
# a single blank space

names = "Ada Bob Charles"
friends = names.split(" ")

print(friends)
for friend in friends:
    print(friend)

# converting a string to a list
# assume each item is seperated by
# a single comma
items = "apple,orange,kiwi"
fruits = items.split(",")

for fruit in fruits:
    print(fruit)
