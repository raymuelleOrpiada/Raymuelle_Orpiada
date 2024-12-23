class Phone:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        
    def __str__(self):
        return f" {self.brand} {self.model} was released year 2018"



class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

iphone= Android("IPhone", "XS Max" )
print(iphone)
        