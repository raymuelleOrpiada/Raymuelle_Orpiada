class Car:
    def __init__(self, brand, color):
        self.brand= brand
        self.color= color
kotse= Car("Honda", "Pink")
print(f"Original Value: {kotse.brand}, {kotse.color}")
kotse.color= ("Red")
print(f"Updated Color: {kotse.color}")

sasakyan=Car("Mirage G4", "Gray")
print(f"Another Car: {sasakyan.brand}, {sasakyan.color}")