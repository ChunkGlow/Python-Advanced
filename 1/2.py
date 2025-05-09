class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

    # Create an instance of Vehicle outside the class definition
modeIX = Vehicle(360, 520000)
print("Model Max Speed:", modeIX.maxspeed)
print("Model Mileage:", modeIX.mileage)