class Employee:

    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Employee Deleted")

    def createObject(self):
        print("Initializing Object")
        obj = Employee()
        print("Object Created")

        return obj
#############################################################

print('Calling createObject() Function....')

emp = Employee()
obj = emp.createObject()

print("Shutting Down....")
exit(0)