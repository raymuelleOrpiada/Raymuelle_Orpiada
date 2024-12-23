class Car:
    def __init__(self, brand, model, fuel_type):
        self.brand= brand
        self.model= model
        self.fuel_type= fuel_type
        
    def __str__(self):
        return f"  {self.brand} {self.model}  is using {self.fuel_type}"

class Car(Car):
    pass
chikot= Car("Honda", "Civic" , "Premium" )
print(chikot)

class Motorcycle(Car):
    pass
broombroom= Motorcycle("Suzuku", "Raider" , "Premium" )
print(broombroom)