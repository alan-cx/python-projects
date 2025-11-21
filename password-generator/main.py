import random
characters = 'abcdefghijklmnopqrstuvwxyz0123456789().-_{}[]=*!'

try:
  length = int(input("Enter password length: "))

  if length <= 0:
    print("Length must be greater than zero.")
    
  else:
    password = ''.join(random.choice(characters) for i in range(length))
    print("Your generated password is:", password)

except ValueError:
  print('THERE HAS BEEN AN ERROR! Please, enter a numerical value')