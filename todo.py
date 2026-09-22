import json

todolist ={

}

reset = '\033[0m'
green = "\033[92m"
red = "\033[91m"
blue = "\033[94m"
yellow = '\033[93m'



while True:
  action = input(f"What do you want to do? ({green}add{reset}/{green} complete{reset}/{green} view{reset}/{green} Delete{reset}/{green} Save{reset}/{green} Load{reset}/{green} quit{reset}: )").lower()

  if action == "quit":
    print(f"{blue}Next time!{reset}")
    break

  elif action == "add":
    todo_name = input("What task would you like to add: ").lower()

    if todo_name in todolist:
      print(f"{red}{todo_name} already exists!{reset}")
    else:
      todolist[todo_name] = "[]"

  elif action == "view":
    if len(todolist) == 0:
      print(f"{red}Your task list is empty!{reset}")
    else:
      for key, value in todolist.items():
        print(f"{yellow}{value}{reset} {blue}{key}{reset}")

  elif action == "complete":
    todo_name = input("Which task do you want to complete: ").lower()

    if todo_name in todolist:
      todolist[todo_name] = "[x]"
      print(f"{green}Task completed!{reset}")

    else:
      print(f"{red}Task not found!{reset}")

  elif action == "delete":
    todo_name_to_delete = input("Enter a task to delete: ").lower()

    if todo_name_to_delete in todolist:
      todolist.pop(todo_name_to_delete)
      print(f"{green}Task successfully deleted{reset}.")

    else:
      print(f"{red}No task found!{reset}")

  elif action == "save":
    with open("todo.txt", "w") as file:
      json.dump(todolist, file)
      print(f"{green}Your tasklist has been successfully saved.{reset}")

  elif action == "load":
    try:
      with open("todo.txt", "r") as file:
        todolist = json.load(file)
        print(f"{blue}You can continue from where you left!{reset}")

    except FileNotFoundError:
      print(f"{red}Oops! You didn't save any tasks yet!{reset}")
  else:
    print(f"{red}Invalid command!{reset}")