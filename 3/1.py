class Vehicle:
    def __init__(self, brand, model, year, color, seats, max_speed, mileage, fuel_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.seats = seats
        self.max_speed = max_speed
        self.mileage = mileage
        self.fuel_type = fuel_type

class Bus(Vehicle):
    pass    

school_bus =  Bus("Mercedes", "Sprinter", 2020, "yellow", 20, 120, 15000, "diesel")

print("Bus Details:")
print("Brand:", school_bus.brand)
print("Model:", school_bus.model)
print("Year:", school_bus.year)
print("Color:", school_bus.color)
print("Seats:", school_bus.seats)
print("Max Speed:", school_bus.max_speed)
print("Mileage:", school_bus.mileage)
print("Fuel Type:", school_bus.fuel_type)
