class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({0},{1})".format(self.x,self.y)
    
p1 = Point(10,20)
print(p1)
