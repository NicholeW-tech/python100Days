from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
} 

def calcultor():
  print(logo)
  num1 = float(input("What is the first number?: "))

  for symbol in operations:
    print(symbol)
    should_continue = True

  while should_continue:
    operation_symbol = input("pick an operation: ")
    num2 = float(input("What is the second number?: "))
    calculation_function= operations[operation_symbol] 
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input("Would you lke to calculate another number? type 'yes' or 'no': ") == "yes":
      num1 = answer
    else:
      should_continue = False
      calcultor()

calcultor()

