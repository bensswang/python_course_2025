class vehical:
    def __init__(self, brand):
        self.brand = brand
    def move(self):
        return "Moving..."

class car(vehical):
    def move(self):
        return "Car is driving"

class bike(vehical):
    def move(self):
        return "Bike is driving"

vehical = [
    car("Toyota"),
    bike("Giant"),
    car("Tesla")
]

for a in vehical:
    print(f"{a.brand} : {a.move()}")
