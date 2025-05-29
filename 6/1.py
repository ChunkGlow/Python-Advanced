class A:
    def __init__(self,a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            print("self is less than other")
        else:
            print("self is not less than other")

    def __eq__(self, other):
        if(self.a == other.a):
            print("self is equal to other")
        else:
            print("self is not equal to other")
##############################################################33

obj1 = A(10)
obj2 = A(3)
print("Passed Values : ", obj1.a, " and ", obj2.a)
print(obj1 < obj2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values :", ob3.a, ob4.a)
print(ob3 == ob4)
