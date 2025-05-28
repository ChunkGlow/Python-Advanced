from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self, x):
        print("Passed value:", x)
        

    @abstractmethod
    def task(self):
        print("We are inside the abstract method")


class test_class(Absclass):
    def task(self):
        print("We are inside the test_class method")
        

test_obj = test_class()
test_obj.task()
test_obj.print(100)