class IOString:
    def __init__(self):
        self.str1 = ""
    
    def getString(self):
        self.str1 = input("Enter a string: ")

    def printString(self):
        print("The string is:", self.str1.upper())

# Example usage

objString1 =  IOString()

objString1.getString()
objString1.printString()
