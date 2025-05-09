class student:

    grade = 8
    age = 13
    name = "Brent"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


o = student("Brent", 13, 8)
print("Student Name: ", o.name)
print("Student Age: ", o.age)
print("Student Grade: ", o.grade)