class Dog():
    # constructor
    def __init__(self, name):
        self.name = name
        self.tricks = []

    # method of dog object
    def add_trick(self, trick):
        self.tricks.append(trick)


# create two Dog objects
dog1 = Dog('Brutus')
dog2 = Dog('Dude')

# call the dogs' method
dog1.add_trick('roll over')
dog1.add_trick('sit')
dog2.add_trick('stay')
dog2.add_trick('roll over')

print("Dog's name: ", dog1.name,
      "\nDog's tricks: ", dog1.tricks)

print("Dog's name: ", dog2.name,
      "\nDog's tricks: ", dog2.tricks)
