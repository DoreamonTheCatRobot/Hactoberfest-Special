# This is an app that will select a random wiki article and provide the summary for you. Then, it will use nlp to select 3 questions about the text that you should answer. 


import wikipedia as wk
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
import random
import os


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
    print("Ok! Here is your text. Read it carefully." )
    print("\n\n"+text)

  process_results = processText(text)

  go = input("\n\nPress 'go' when you are ready to start. ")
  while  go != "go":
    print("Ooops, I don't understand that. Press 'Go' to start.")
    go = input("\n\nPress 'go' when you are ready to start. ")
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    gameplay_menu(process_results)


def gameplay_menu(process_results):
  print("Fill in the blanks by entering the missing words. (Not case sensitive.) \nPress 'freebie' to get an answer.\nPress '**' to quit.")
  print("\n\n"+process_results[0])
  guess = ""
  while guess != "**" and process_results[1]:
    guess = input("\nNext guess?\n")
    if guess in process_results[1]:
      print("Yes! You got one!")
      process_results[1].remove(guess)
    elif guess == "freebie":
      print(process_results[1][0])
      process_results[1].remove(process_results[1][0])
      print("Ok, that one was free.")
    else: 
      print("Ehh, not quite. Try again!\n")

  if guess == "**":
    print("Ok! Here were the missing words")
    for leftover in process_results[1]:
      print(leftover)
    print("Come back tomorrow for more fun!")
    exit()
  if process_results[1] == []:
    print("Congrats! You won!! \n\n")
    contin = input("Want to play again?").lower()
    if contin == "yes":
      getRandomPgs()
    else:
      print("Come back tomorrow for more fun!")
      exit()



def processText(text):
  tagged_words = []
  relevant_words = []
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
      if w[0] in relevant_words:
        pass
      else:
        relevant_words.append(w[0])

  #print("relevant_words: ", relevant_words)
  
  
  qq=1
  randQQ = []
  while qq <4:
    temp = random.choice(relevant_words)
    if temp in randQQ:
      pass
    else:
      randQQ.append(temp)
      qq=qq+1
  #print("randQQ: ",randQQ)

  newtext=text
  for QQ in randQQ:
    #print("QQ: ", QQ)
    newtext=newtext.replace(QQ, "_________")

    
  return [newtext, randQQ]



if __name__ == '__main__':
  main()