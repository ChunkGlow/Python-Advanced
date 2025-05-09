class Parrot:

    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Red = Parrot("Red", 2)
Orange = Parrot("Orange", 3)

print("Red is a {}".format(Red.__class__.species))
print("Orange is a {}".format(Orange.__class__.species))

print("{} is {} years old".format(Red.name, Red.age))
print("{} is {} years old".format(Orange.name, Orange.age))
