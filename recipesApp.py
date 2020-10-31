# App to select recipes and consolidate ingredients into a shopping list




selectedRecipes = []
recipes = []
def main():
  # Instantiate recipes
  recipes.append(Recipe("Meaty Spaghetti", 15, [{"thin spaghetti": 9,"mushroom and garlic pasta sauce" : 16, "ground beef" : 16, "parmesean cheese": 4, "baguette" : 1, "garlic": 1}]))
  recipes.append(Recipe("Cheese Tortellini", 10, [{ "cheese torellini": 10, "pesto sauce" : 8, "parmesean cheese" : 3, "spinach":6, "oil & vinegar" : 2, "roma tomatoes" : 2}]))
  recipes.append(Recipe("Tacos!", 20, [{"taco shells" : 8,"ground beef": 10,"roma tomatoes" : 3, "cheddar cheese" : 4, "guac" : 6}]))
  print("Welcome to the Grocery List Consolidator!\n\nSelect a dish to preview the ingredients.")
  
  mainMenu()

# menu to select dishes
def mainMenu():
 
  r = 1
  for recipe in recipes:
    print(str(r)+". - "+recipe.name + "\n")
    r=r+1

  makeSelection()


def makeSelection():
  selection = int(input())

  #if selection == "2": 
  recipes[selection-1].display()
  addDecision = input("Do you want to add this recipe to your shopping list? [Yes / No]\n").lower()
  if addDecision == "y" or addDecision == str("yes"):
    selectedRecipes.append(recipes[selection-1])
    recipes.remove(recipes[selection-1])
    print("In your list: \n")
    for recipe in selectedRecipes:
      print(recipe.name)


  while recipes != []:
    print("Do you want to add another dish?")
    contin = input().lower()

    if contin == "yes":
      mainMenu()
    elif contin == "no":
      if selectedRecipes != []:
        print("Great! Preparing your shopping list now...")
        printShoppingList()
      else:
        print("Looks like your shopping list is empty. Come back and select some recipes soon!")
    else: 
      while contin != "yes" and contin != "no":
        print("Hmm - cooking can be confusting. Try that again. :) ")
        contin = input("Do you want to add another dish?\n")
    
    print("You've selected all the available recipes. I'll go ahead and prepare your shopping list for you. ")
    printShoppingList()



def printShoppingList():
  items = {}
  for selectedRecipe in selectedRecipes:
    for ingrs in selectedRecipe.ingredients:
      for ingr in ingrs:
        if ingr not in items:
          items[ingr] = ingrs[ingr]
        else:
          print("adding", ingr)
          currval = items[ingr]
          print("currval", currval)
          newval = currval + ingrs[ingr]
          print('newval', newval)
          items[ingr] = newval
  
  print("========+++++++++  SHOPPING LIST  ++++++++++===========")
  for item in items:
    print(str(items[item])+ " - " + item)

  exit()

class Recipe: 
  def __init__(self, name, prepTime, ingredients):
    self.name = name
    self.prepTime = prepTime
    self.ingredients = ingredients

  def display(self):
    print(self.name)
    print("Prep Time: "+str(self.prepTime))
    for ingredient in self.ingredients:
      for key in ingredient:
        print(str(ingredient[key]) +" - " + key)



if __name__ == "__main__":
  main()