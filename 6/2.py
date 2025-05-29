class Flashcard:
  def __init__(self, word, definition):
    self.word = word
    self.definition = definition

  def __str__(self):
    return self.word + '(  ' + self.definition + '  )'



flash = []
print("Welcome to the flashcard app!")

while (True):
  word = input("Enter a name that you want to add to the flashcard: ")
  definition = input("Enter the definition of the word: ")

  flash.append(Flashcard(word, definition))

  option = int(input("Enter 1 to add another flashcard, 2 to see all flashcards, or 3 to exit:"))

  if(option):
    break

# printing all the flashcards
print("\nYour flashcards")
for i in flash:
  print(">", i)

  