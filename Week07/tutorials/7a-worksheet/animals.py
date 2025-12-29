class Animal():
    # constructor
    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed

    # to string method, used for printing the object
    def __str__(self):
        return self.name + "|" + self.dob + "|" + self.colour + "|" + self.breed

    def printit(self):
        print("Name: ", self.name)
        print("DOB: ", self.dob)
        print("Colour: ", self.colour)
        print("Breed: ", self.breed)
        print("Class: ", self.myclass)
        print(self)

    def sound(self):
        print(self.name, "has no sound!")


class Dog(Animal):
    myclass = 'Dog'
    
    def __init__(self, name, dob, colour, breed):
        # call super class Animal __init__ (i.e. Constructor)
        super().__init__(name, dob, colour, breed)

    # override sound() method in super class
    def sound(self):
        # name is inherited from Animal
        print(self.name, "Woof Woof")

class Cat(Animal):
    myclass = 'Cat'

    # NOTE: There is no __init__ constructor

    # override sound() method in super class
    def sound(self):
        print(self.name, "Meow Meow")

class Bird(Animal):
    myclass = 'Bird'


def main():
    # call the __init__ in dog
    dog = Dog('Snoopy', '10-Aug-1968', 'white', 'beagle')
    dog.printit() # printit() is inherited from Animal
    dog.sound()
    print()

    # NOTE: there is no __init__ in Cat
    # Python will call the __init__ directly from Animal instead
    cat = Cat('Garfield', '19-June-1987', 'orange', 'Persian')
    cat.printit() # printit() is inherited from Animal
    cat.sound()
    print()

    bird = Bird('Big Bird', '20-March-1969', 'yellow', 'Canary')
    bird.printit() # printit() is inherited from Animal
    bird.sound() # sound() is inherited from Animal
    print()

if __name__ == '__main__':
    main()
