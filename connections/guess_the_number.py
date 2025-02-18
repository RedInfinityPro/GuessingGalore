import random

points = 0
MaximNumber = 9
currentTries = 0
RandomizedNumber = random.randint(0,MaximNumber)

while True:
  try:
    userInput = int(input("\nyour points: {} \nGuess number between {} - {} > ".format(points,0,MaximNumber)))
    if currentTries < 3 and userInput != RandomizedNumber:
      currentTries += 1
      print("you have {} tries left before you loose points".format(4 - currentTries))
      if userInput > RandomizedNumber:
        print("guess lower")
      elif userInput < RandomizedNumber:
        print("guess higher")
    elif currentTries == 3 and userInput != RandomizedNumber:
      if points > 0:
        points -= 1
        print("you current points is now {}".format(points))
      else:
        print("sorry you lost the game")
    else:
      points += 1
      print("correct! The number was {} \n points {}".format(RandomizedNumber,points))
      RandomizedNumber = random.randint(0,MaximNumber)
      currentTries = 0
      MaximNumber *= 2
  except ValueError:
    print("sorry, your input is not a number")
