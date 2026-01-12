class Car():
    def __init__(self, driver, passangers):
        # driver and passanger are passed in
        self.driver = driver
        self.passangers = passangers

    def printit(self):
        print(self.driver)
        for passanger in self.passangers:
            print(passanger)

class Person():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

if __name__ == '__main__':
    driver = Person('Driver')
    p1 = Person('P1')
    p2 = Person('P2')
    passangers = [p1, p2]

    car = Car(driver, passangers)
    car.printit()

    # destroy car
    car = None
    # objects created outside car ar enot destroyed
    print(driver)
    for p in passangers:
        print(p)
