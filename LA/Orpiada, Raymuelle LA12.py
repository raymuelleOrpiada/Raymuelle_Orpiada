class Toy:
    def __init__(self, name, price):
        self.name= name
        self.price= price
    
    def describeToy(self):
        print (f" {self.name} is costing around {self.price}")
    


class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
Toy= Car("Lightning MCQueen", 10000 )
Toy.describeToy()
        