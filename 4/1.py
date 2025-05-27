class myClass:

    __privateVar = 20;

    def __privMeth(self):
        print("This is a private method")

    def text(self):
        print("Public Value : ", myClass.__privateVar)

    
foo = myClass()
foo.text()
foo.__privMeth()
