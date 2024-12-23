class Animal:
    def __init__(self, name, types , can_swim):
        self.name= name
        self.types= types
        self.can_swim=can_swim
    
    

class Fish(Animal): 
    def __init__(self, name, types , can_swim):
        super().__init__(name, types , can_swim)
        self.can_swim= True

Tilapia=Fish("Tilapia", "Masarap na isda", True)
print(Tilapia.can_swim)