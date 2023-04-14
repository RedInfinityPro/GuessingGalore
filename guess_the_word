from random_word import RandomWords
import nltk
from nltk.corpus import wordnet
# get random word and def
def Get_Word():
  fullWord = []
  while True:
    try:
      word = RandomWords()
      word = word.get_random_word()
      word_to_define = word + '.n.01'
      define = wordnet.synset(word_to_define).definition()
    except:
      pass
    else:
      fullWord = [word,define.replace(word,"___")]
      return fullWord
      break

get_word = Get_Word()
# loop
points = 0
Incorect_Times = 3
def give_hint(word,Incorect_Times):
  hintString = ''
  for i in range(0,len(word)):
    if i <= len(word)//3:
      hintString = hintString + word[i]
  return hintString
    
while points > -1:
  try:
    print('The definition is: "{}"'.format(get_word[1]))
    userInput = input("> ")
    if userInput != get_word[0]:
      print('sorry "{}" is not the word'.format(userInput))
      if Incorect_Times > 0:
        Incorect_Times -= 1
        print('hint: "{}"'.format(give_hint(get_word[0],Incorect_Times)))
      else:
        points -= 1
    else:
      Incorect_Times = 3
      get_word = Get_Word()
  except:
    print("It's sad to se you go")
    break
  
else:
  print('Sorry, you have lost \nThe word was "{}"'.format(get_word[0]))
