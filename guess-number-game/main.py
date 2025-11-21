import random

print('**Welcome to Guess the Number Game**')
print('Try to guess the number in five attempts')

while True:
  try:
    option = int(input("\n1. Play\n2. Exit\nChoose an option: "))
  except ValueError:
    print("Please enter a valid number")
    continue

  if option == 1:
    random_number = random.randint(1, 10)
    attempts = 5

    for attempt in range(attempts):
      try:
        guess = int(input("Enter a number between 1 and 10: "))
      except ValueError:
        print("Invalid input. Try again.")
        continue  

      if guess == random_number:
        print(f"Congratulations! The number was {random_number}!")
        break
      
      elif guess > random_number:
        print("Too high.")
        
      else:
        print("Too low.")
                
    else:
      print(f"You lost! The number was {random_number}.")

  elif option == 2:
    print("Bye!")
    break

  else:
    print("Choose a valid option (1 or 2).")
