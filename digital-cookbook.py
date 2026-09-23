import json

cookbook = {

}

red = '\033[91m'
reset = '\033[0m'
blue = '\033[94m'
green = '\033[92m'

while True:
  action = input(f"What do you want to do?{green} Recipe{reset}/{green} Ingredient{reset}/{green} Read{reset}/{green} Save{reset}/{green} Load{reset}/{green} Quit{reset} ").lower()

  if action == 'quit':
    print(f"{blue}Goodbye!{reset}")
    break

  elif action == 'recipe':
    recipe_name = input("What is the name of the recipe? ").lower()

    if recipe_name in cookbook:
      print("Recipe already exist!")

    else:
      cookbook[recipe_name] = []

  elif action == 'ingredient':
    recipe_name = input("What is the name of the recipe? ").lower()
    if recipe_name in cookbook:
      item = input("What ingredient do you want to add?")
      cookbook[recipe_name].append(item)
      print("Ingredient successfully added!")
    else:
      print("Recipe not found!")

  elif action == 'read':
    recipe_name = input("What recipe do you want to search for? ").lower()

    if recipe_name in cookbook:
      for values in cookbook[recipe_name]:
        print(f"To cook {recipe_name}, you need {blue}{values}{reset}")

    else:
      print(f"{red}Recipe doesn't exist!{reset}")

  elif action == 'save':
    with open ("recipes.txt", "w") as file:
      json.dump(cookbook, file)
      print(f"{green}Recipe name successfully saved!{reset}")

  elif action == 'load':
    try:
      with open("recipes.txt", "r") as file:
        cookbook = json.load(file)
        print("The recipe has been successfully loaded!")
    except FileNotFoundError:
      print(f"{red}There is no saved file!{reset}")

  else:
    print(f"{red}Invalid{reset}")
