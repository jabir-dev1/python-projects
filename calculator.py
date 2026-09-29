reset = '\033[0m'
green = "\033[92m"
red = "\033[91m"
blue = "\033[94m"
yellow = "\033[93m"


def carry_out_calculation(number1, number2 ,sign):
 if sign == "+":
  return number1 + number2
  
 elif sign == "-":
  return number1 - number2
  
 elif sign == "*":
  return number1 * number2
  
 elif sign == "/":
   try:
     return number1 / number2
     
   except ZeroDivisionError:
     print("You cannot divide by zero")

 
def print_result(a, b,c, returned_value):
  if returned_value is None:
    print("You can't divide by zero")
  else:
     print(f"{blue}{a}{reset} {c} {blue}{b}{reset} = {blue}{returned_value}{reset}")


while True:
  print(f"{yellow}-------{reset} {green}CALCULATOR{reset}{yellow}--------{reset}")
  action = input(f"Enter {red}'quit'{reset} to exit:").lower()

  if action == "quit":
    break
  else:
    operator = input(f"{green}Enter an operator(+ - * /):{reset} ")
    valid_operators = ["+", "-", "*", "/"]
    while operator not in valid_operators:
      print(f"{red}That is not an operator!{reset}")
      operator = input(f"{green}Enter an operator(+ - * /):{reset} ")
   
    while True:
      try:
        numb1 = float(input(f"{green}Enter the first number:{reset} "))
        break
      except ValueError:
        print(f"{red}Type in a number!{reset}")
    while True:
      try:
         numb2 = float(input(f"{green}Enter the second number:{reset} "))
         break
      except ValueError:
        print(f"{red}Type in a number!{reset}")
    
    result = carry_out_calculation(numb1, numb2, operator)
    print_result(numb1, numb2, operator, result)
   

