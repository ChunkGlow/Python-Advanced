class Bird:
    
    def __init__(self):
        print("Bird is Ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")


class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is Ready")
    def whoisThis(self):
        print("Penguin")
    def swim(self):
        print("Swim slower")
    def run(self):
        print("Run faster")

peggy = Penguin()

peggy.whoisThis()
peggy.swim()
peggy.run()

