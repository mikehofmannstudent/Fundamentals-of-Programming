class Car():
    def __init__(self, driver, passengers):
         self.driver = driver
         self.passengers = passengers

    def __str__(self):
        return "Driver: " + self.driver + "\nPassengers: " + str(self.passengers)

driver = "Peter"
passengers = ["John", "Bob"]
car = Car(driver, passengers)
print(car)

# destroy car
car = None
print(car)

# driver and passengers still exist
print(driver)
print(passengers)
