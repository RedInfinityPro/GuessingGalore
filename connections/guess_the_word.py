import re
import nltk
import time
import random
from random_word import RandomWords
from nltk.corpus import wordnet
nltk.download('wordnet')
word_generator = RandomWords()
current_time = time.time()
random.seed(current_time)

# add to the dictionary
def build_dictionary(PATH, addWord_amount, dictionary):
  attempts = 3 # Assuming 'word_generator' has a limitation of words it can use
  added_count = 0  # Track how many words were successfully added
  try:
    if attempts > 0:
      for amount in range(addWord_amount):
        while True: 
          word = word_generator.get_random_word()
          if word and re.match(r"^[a-zA-Z0-9.,'!?-]+$", word):
            synset = wordnet.synsets(word, pos=wordnet.NOUN)
            if synset: # check if word has definition
              if word not in dictionary: # check if word is in definition
                definition = synset[0].definition()
                with open(PATH, 'a', encoding='utf-8') as dictionary:
                  dictionary.write(f"\n{word}: {definition}\n")
                # Update dictionary & counter
                dictionary = read_dictionary(r'dictionary.txt')
                added_count += 1
                break
            else:
              print(f"We tried '{word}', however this word's definition was not found. You have {amount}/{addWord_amount} words left.")
    else:
      print("[Closed]: To many repetitive items found in the dictionary file")
  except FileNotFoundError:
    print(f"Error: File '{PATH}' not found")
    return {}
  except Exception as e:
    print(f"Error reading file: {str(e)}")
    return {}

# read dictionary
def read_dictionary(PATH):
  dictionary = {}
  try:
    with open(PATH, 'r', encoding='utf-8') as f:
      lines = f.readlines()
      for line in lines:
        if not line.strip():
          continue
        parts = line.strip().split(': ', 1)
        # Only process lines that have both word and definition
        if len(parts) == 2:
          word = parts[0].strip()
          definition = parts[1].strip()
          dictionary[word] = definition
  except FileNotFoundError:
    print(f"Error: File '{PATH}' not found")
    return {}
  except Exception as e:
    print(f"Error reading file: {str(e)}")
    return {}
  return dictionary

build_dictionary(r'dictionary.txt', 10, read_dictionary(r'dictionary.txt'))
dictionary = read_dictionary(r'dictionary.txt')
print(dictionary)