print("**Welcome to Arithmetic Calculator**")
print("\nOperations")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

def sum(a, b): print(a+b)
def sub(a, b): print(a-b)
def multi(a, b): print(a*b)

def division(a, b):
  if b == 0:
    print("Divider cannot be zero, enter a different value!")
    return
  print(a / b)

operations = {
  1: sum,
  2: sub,
  3: multi,
  4: division
}

def get_numbers():
  try:
    a = int(input('A: '))
    b = int(input('B: '))
    return a, b

  except:
    print("Enter valid numbers")
    return None, None

while True:
  try:
    user_decision = int(input('Choose an operation: '))
  except:
    print('Enter a valid number')
  
  if user_decision == 5:
    print('Bye!')
    break
    
  if user_decision in operations:
    a, b = get_numbers()
    if a is not None:
      operations[user_decision](a, b)

  else:
    print('Please, select a valid option!')
