from animals import Dog, Cat, Bird

# This is to model a Animal shelter
# Animal shelter is a place to keep "unwanted" pets
# The animals will be put up for public adoption

class Shelter():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        # this list store the animals that
        # just came into the shelter
        self.processing = []
        # after the animal has been "processed" (e.g. vaccinated)
        # it will be transfered to "available"
        self.available = []
        # after the animal is adopted by the public
        # it will be transfered to "adopted"
        self.adopted = []

    def newAnimal(self, type, name, dob, colour, breed):

        temp = None
        if type == 'Dog':
            temp = Dog(name, dob, colour, breed)
        elif type == 'Cat':
            temp = Cat(name, dob, colour, breed)
        elif type == 'Bird':
            temp = Bird(name, dob, colour, breed)
        else:
            print('Error, unknown animal type: ', type)

        if temp:
            self.processing.append(temp)
            print("Added ", name, " to processing list")

    def makeAvailable(self, name):
        for animal in self.processing:
            if(animal.name == name):
                self.available.append(animal)
                self.processing.remove(animal)

    def makeAdopted(self, name):
        for animal in self.available:
            if(animal.name == name):
                self.adopted.append(animal)
                self.available.remove(animal)
    def displayProcessing(self):
        print("Displaying Processing")
        for animal in self.processing:
            animal.printit()

    def displayAvaliable(self):
        print("Displaying Avaliable")
        for animal in self.available:
            animal.printit()

    def displayAdopted(self):
        print("Displaying Adopted")
        for animal in self.adopted:
            animal.printit()

    def displayAll(self):
        self.displayProcessing()
        print()
        self.displayAvaliable()
        print()
        self.displayAdopted()
