import random

class FruitQuiz:
  def __init__(self, fruits):
    self.fruits = {'apple': 'red', 
                   'banana': 'yellow', 
                   'orange': 'orange', 
                   'grape': 'purple', 
                   'mango': 'yellow'}

  def quiz(self):
    while True:

      fruit, color =  random.choice(list(self.fruits.items()))
      print("What is the color of a {}".format(fruit))
      a = input("Enter the color: ")

      if(a.lower() == color):
        print("Correct!")
      else:
        print("Wrong! The correct answer is {}".format(color))

      option = int(input("Enter 1 to continue or 2 to exit: "))
      if(option):
        break
      
      
print("Welcome to the fruit quiz!")
fq = FruitQuiz()
fq.quiz()