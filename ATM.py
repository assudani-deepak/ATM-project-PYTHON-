ascii_art = """
 _=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_
|                                         |
|     _____     ____    _____    _____    |
|    |_ " _| U | __") u|_ " _|  |" ___|   |
|      | |    \|  _ \/   | |  U | |_  u   |
|     /| |\    | |_) |  /| |\  \|  _|/    |
|    n |_| n   |____/  n |_| n  |_|       |
|                                         |
|=========================================|
|                                         |
|       Welcome to TBTF Banking!          |
|                                         |
|    Please select from one of the        |
|    below options:                       |
|                                         |
|      1. Display Balance                 |
|      2. Withdraw funds                  |
|      3. Deposit Funds                   |
|      9. Return Card                     |
|                                         |
|                                         |
 ‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾=‾
"""

import os # Import the os module for clearing the screen
from time import sleep
user_pin = 123456
pin_attempt = 0
balance = 1000
tasks = 0
user_access = True

print("Welcome to TBTF Banking!\n")
while True:
  input_pin = int(input("Please enter your 6-digit PIN: "))
  if input_pin != user_pin:
    if pin_attempt < 2:
      pin_attempt += 1
      print("\nIncorrect PIN. Please try again.\n")
      print("You have", 3 - pin_attempt, "attempt(s) left.\n")
      
    else:
      print("\nToo many incorrect attempts. Please try again later\n")
      print("Please take your card")
      user_access = False
      break
  else:
    print("PIN accepted")
    break
  
while user_access:
  print("\nPlease hold...\n")
  sleep(3)
  os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
  print(ascii_art)
  input_main_menu = int(input("Enter your option:\n\n"))

  if input_main_menu == 1:
    tasks += 1
    print("\nYour current balance is £", balance, "\n")
    input("Press any key to go back to the main menu\n")
    print("You will now be returned to the main menu\n")

  dict_cash_withdraw = {1: 10, 2: 20, 3: 40, 4: 60, 5: 80, 6: 100}
  
  if input_main_menu == 2:
    print("\nPlease select withdrawal amount")
    for key, value in dict_cash_withdraw.items():
      print(f"{key} - £{value}")
    print("7 - Other amount")
    print("8 - Return to main menu")
    input_cash_withdraw = int(input())
    
    if input_cash_withdraw in range(1, 7):
      withdrawal_amount = dict_cash_withdraw[input_cash_withdraw]
      if withdrawal_amount > balance:
        print("Insufficient funds")
      else:
        balance -= withdrawal_amount
        tasks += 1
        print(f"You have withdrawn £{withdrawal_amount} from your account")
        print("Please take your cash.")
        print("Your new balance is £", balance, "\n")
        input("Press any key to go back to the main menu\n")
        print("You will now be returned to the main menu\n")
  
    elif input_cash_withdraw == 7:
      while True:
        input_withdraw_custom = int(input("How much would you like to withdraw? £ "))
        if input_withdraw_custom > balance:
          print("\nInsufficient funds\n")
        elif input_withdraw_custom <= balance:
          if input_withdraw_custom % 10 != 0:
            print("Please enter a number in multiples of 10\n")
          if input_withdraw_custom % 10 == 0:
            balance -= input_withdraw_custom
            tasks += 1
            print("You have withdrawn £", input_withdraw_custom,
                  "from your account, please take your cash.")
            print("Your new balance is £", balance, "\n")
            input("Press any key to go back to the main menu\n")
            print("You will now be returned to the main menu\n")
            break
    
    elif input_cash_withdraw == 8:
      print("You will now be returned to the main menu\n")

  if input_main_menu == 3:
    while True:
      print("How much would you like to deposit?")
      print("If you wish to return to the previous menu, please enter 0")
      try:
        input_deposit = int(input("£ "))
        if input_deposit == 0:
          print("You will now be returned to the main menu\n")
          break
        elif input_deposit in range(1, 10):
          print ("The minimum deposit amount is £10")
        elif input_deposit >= 10:
          cashreturn = input_deposit % 10
          balance = balance + input_deposit - cashreturn
          tasks += 1
          print("£", input_deposit - cashreturn, "has been deposited.\n")
          if input_deposit % 10 != 0:
            print("You can only deposit a number in multiples of 10, £", cashreturn,
                  "has been returned to you.\n")
          print("your new balance is £", balance, "\n")
          input("Press any key to go back to the main menu\n")
          print("You will now be returned to the main menu\n")
          break
      except ValueError:
        print("\nPlease enter a valid amount/option\n")

  if input_main_menu == 9:
    user_access = False
    print("\nPlease take your card\n")
    print("You have completed", tasks, "tasks today with us.\n")
    print("We hope you are satisfied with our service and")
    print("look forward to your next visit.\n")
    print("Goodbye!")
    break