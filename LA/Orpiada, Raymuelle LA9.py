class Car:
    def __init__(self, brand):
        self.brand= brand
    def __str__(self):
        return f"{self.brand} is a car object"
car = Car("BMW")
print(car)
del(car)
print(car)