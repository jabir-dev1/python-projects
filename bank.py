#bank simulator without using classes
import random
import json


green = "\033[92m"
red = "\033[91m"
blue = "\033[94m"
reset = "\033[0m"
yellow = "\033[93m"


bank_account = {}

def create_account_name():
  account_name = input(f"{green}Enter your name:{reset} ").lower().strip()
  while account_name == "":
    print(f"{red}Type in your name!{reset}")
    account_name = input(f"{green}Enter your name:{reset} ").lower().strip()
  return account_name

def validate_name():
  name = input(f"{green}Enter your name:{reset} ").lower().strip()
  while name == "":
    print(f"{red}Type in your name!{reset}")
    name = input(f"{green}Enter your name:{reset} ").lower().strip()
  return name



def generate_account_number(dictionary_name):
  number = random.randint(100000,999999)
  while number in dictionary_name:
    number = random.randint(100000,999999)
  return number



def get_amount():
  while True:
    try:
      amount = float(input(f"Enter how much you would like to {green}deposit{reset}/ {green}withdraw{reset}/ {green}transfer{reset}: "))
      if amount <= 0:
        print(f"{red}Amount must be greater than 0!{reset}")
        continue
      break
    except ValueError:
      print(f"{red}Enter a number!{reset}")
  return amount







def deposit_money(dictionary):
  name = input(f"{green}Enter your name:{reset} ").lower().strip()
  while name == "":
    print(f"{red}Type in a valid name!{reset}")
    name = input(f"{green}Enter your name:{reset} ").lower().strip()
  is_available = False
  for account_number, account_info in dictionary.items():
    if name == account_info['account_name']:
      amount = get_amount()
      account_info['account_balance'] += amount
      for items in account_info['transactions']:
        items['deposited'].append(amount)
      print(f"You have succesfully deposited {blue}${amount}{reset}")
      is_available = True
  if is_available == False:
    print(f"{red}Your name doesn't exist!{reset}")

def withdraw(dictionary_name):
  name = validate_name()

  for account_number, account_info in dictionary_name.items():
    if name == account_info['account_name']:
      amount = get_amount()
      if account_info['account_balance'] >= amount:
        account_info['account_balance'] -= amount
        for items in account_info['transactions']:
          items['withdrawn'].append(amount)
        print(f"You have withdrawed {blue}${amount}{reset} from your bank account")
      else:
        print(f"{red}You don't have sufficient funds!{reset}")
        
        

def transfer_money(dictionary):
  name = validate_name()
  is_recipient_name_available = False
  is_amount_enough = False
  for account_number, account_info in dictionary.items():
    if name == account_info['account_name']:
      receivers_name = input(f"{green}Enter the name of the recipient:{reset} ").lower().strip()
      while receivers_name == "":
        print(f"{red}Type a name!{reset}")
        receivers_name = input(f"{green}Enter the name of the recipient:{reset} ").lower().strip()
      
      for number_of_recepient, account_details_of_recipient in dictionary.items():
        if receivers_name == account_details_of_recipient['account_name']:
          is_recipient_name_available = True
          amount = get_amount()
          if account_info['account_balance'] >= amount:
            is_amount_enough = True
            for items in account_info['transactions']:
              items['transferred'].append(amount)
            for items in account_details_of_recipient['transactions']:
              items['received'].append(amount)      
            account_details_of_recipient['account_balance'] += amount
            account_info['account_balance'] -= amount
            print(f"You have sent money to {blue}{receivers_name}{reset}")
  
  if is_recipient_name_available == False:
    print(f"{red}That account doesn't exist!{reset}")
  if is_recipient_name_available == True and is_amount_enough == False:
    print(f"{red}You don't have sufficient money{reset}")


while True:
  
  command = input(f"{green}Create{reset}/ {green}Deposit{reset} / {green}Withdraw{reset}/ {green}check balance{reset}/ {green}Transfer money{reset}/ {green}View Transaction history{reset}/ {green}Save{reset}/{green}Load{reset}/{green} quit{reset}: ").lower().strip()

  if command == "quit":
    print(f"{blue}Closed")
    break

  elif command == "create":
    acccount_number = generate_account_number(bank_account)
    name = create_account_name()
    print(acccount_number)

    bank_account[acccount_number] = {
      "account_name": name,
      "account_balance": 0,
      "transactions": [{
        'deposited':[],
        'withdrawn': [],
        'transferred': [],
        'received':[]
      }]
    }
    

  elif command == "deposit":
   deposit_money(bank_account)
  
  elif command == "withdraw":
    withdraw(bank_account)

  elif command == "balance":
    name = validate_name()
    name_is_available = False
    for account_number, account_info in bank_account.items():
      if name == account_info['account_name']:
        name_is_available = True
        print(f"Your balance is {blue}${account_info['account_balance']}{reset}")
    if name_is_available == False:
      print(f"{red}You don't have an existing bank account!{reset}") 




  elif command == "transfer":
    transfer_money(bank_account)

  elif command == "view":
    name = validate_name()
    is_name_available = False
    for keys, values in bank_account.items():
      if name == values['account_name']:
        is_name_available = True
        for items in values['transactions']:
          print(f"{yellow}Deposited{reset}: {blue}${items['deposited']}{reset}")
          print(f"{yellow}Withdrawn{reset}: {blue}${items['withdrawn']}{reset}")
          print(f"{yellow}Transferred{reset}: {blue}${items['transferred']}{reset}")
          print(f"{yellow}Received{reset}: {blue}${items['received']}{reset}")

    if is_name_available == False:
      print(f"{red}Create an account first{reset}")

  elif command == "save":
    with open("bankaccount.json", "w") as file:
      json.dump(bank_account, file)
      print(f"{green}Data successfully saved{reset}")

  elif command == "load":
   try:
     with open("bankaccount.json", "r") as file:
       bank_account = json.load(file)
       print(f"{green}Data loaded successfully!{reset}")
   except FileNotFoundError:
     print(f"{red}File not found! Ensure you saved your details{reset}")
  else:
    print(f"{red}Invalid command{reset}")