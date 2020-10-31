# This is an app that will select a random wiki article and provide the summary for you. Then, it will use nlp to select 3 questions about the text that you should answer. 


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

    processText(text)



def processText(text):
  tagged_words = []
  summTokenSenten = sent_tokenize(text)
  for sentence in summTokenSenten:
    summTokenWord = word_tokenize(text)
    for word in summTokenWord:
      tagged_words = nltk.pos_tag(summTokenWord)
    NER = nltk.ne_chunk(tagged_words, binary= True)
    #print(NER)
    #print(tagged_words)
  for w in tagged_words:
    if w[1] == "NNP" or w[1] == "CD":
      print(w)

  qq=1
  randQQ = []
  while qq <4:
    randQQ.append(random.choice(tagged_words))
    qq=qq+1
  print("randQQ: ",randQQ)



if __name__ == '__main__':
  main()