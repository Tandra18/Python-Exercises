#Create a child class Bus that will inherit
# all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self,name, model, brand):
        self.name = name
        self.model = model
        self.brand = brand

class Saloon(Vehicle):
    pass
mycar = Saloon("Yaris",2019,"Toyota")
print("Car name :"+mycar.name+ f"\nModel :[{mycar.model}]"+"\nBrand :"+mycar.brand)