#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of
# Bus.seating_capacity() a default value of 50.
# Expected Output:
#
# The seating capacity of a bus is 50 passengers

class Vehicle :
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seatingCapacity(self,capacity):
        return f"The seating capacity of {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seatingCapacity(self,capacity = 50) :
        return super().seatingCapacity(capacity = 50)

School_bus = Bus("School Volvo", 250, 60)
print(School_bus.seatingCapacity())