class Appliance:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    def operate(self):
        print (f"Operating!")
        
    def info(self):
        print (f"{self.brand} is {self.model} model")

class WashingMachine(Appliance):
    def operate(self):
        print ("Washing clothes!")
        
   

class Refrigerator(Appliance):
    def operate(self):
        print ("Keeping food cold!")
        
   
        
class Microwave(Appliance):
    def operate(self):
        print ("Heating Food!")
    
    
        
wm= WashingMachine("Haier", "Whirpool")
ref= Refrigerator("LG", "Family Hub")
mw=Microwave("Samsung", "L456413")

for app in (wm, ref,mw):
    app.operate()
    app.info()