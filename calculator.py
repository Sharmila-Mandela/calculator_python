def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):

    if b == 0:
        return "Division by zero is not allowed."
    return a / b
def power(a,b):
  return  a**b
continue_calculating=True
while continue_calculating is True:
  
  num1 = float(input("Enter the first number: "))

  num2 = float(input("Enter the second number: "))


  operation = input("Enter the operation (+, -, *, /,^): ")

  if operation == "+":
      print(add(num1, num2))
  elif operation == "-":
      print(subtract(num1, num2))
  elif operation == "*":
      print(multiply(num1, num2))
  elif operation == "/":
      
      print(divide(num1, num2))
  elif operation == "^":
      print(power(num1,num2))
  else :
     print("Invalid operation.")
    
  yes_or_no = input('Continue?(y/n):')
  if yes_or_no =='n':
    continue_calculating=False     
