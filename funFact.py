# This is an app that will privide random wiki articles and let you select what you want to read about
import wikipedia as wk
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
nltk.download('words')
import random


def main():

  print("Welcome to the Wikipedia Random Facts Quiz Game! \n")
  getRandomPgs()





def getRandomPgs():
  randPgs = wk.random(pages=5)
  print("Select one of the random topics below to start the game, or press 9 to Generate New Topics.\n\n" )
  i = 1
  for pg in randPgs:
    print(str(i) + " - "+pg)
    i=i+1
  print("9 - Generate 5 New Topics")

  collectData(randPgs)





def collectData(randPgs):
  # Enhancement: Do some input validation here
  selection = int(input())
  if selection == 9:
    getRandomPgs()
  else:
    text = wk.summary(randPgs[selection-1])
    print("Ok! Here is your text. Read it carefully, and when you are ready for your quiz questions, type Go!")
    print("\n\n"+text)
    print("\n\nDo you want to read about something else?")
    contin = input("Yes or No?").lower()
    ## Enhancement: More error handling
    if contin == "yes":
      getRandomPgs()
    else:
      exit()



   


if __name__ == '__main__':
  main()