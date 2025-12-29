class Car():
    def __init__(self):
        self.wheels = 4
        self.engine = 'ESS'

    def __str__(self):
        return "Wheel: " + str(self.wheels) + "Engine: " + self.engine

car = Car()
print(car)
# destroy the car object
car = None
print(car)
