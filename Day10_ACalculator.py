#Here we are defining the operations in the form of functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return round(n1 / n2,2)
#created a playbook for all the operations our calculator can perform in the form of a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
#main recursive loop begins
def calculator():
  num1 = float(input("What's the first number?: "))
#displays user the keys of operations directory so that he can choose a symbol
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:

    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
#for invoking function, we combine operations and pass the key(operation_symbol) here
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
#if user wishes to do further calculations in continuation of the answer from first time
    choice=input("To continue type 'y' else type 'n' :")
    if  choice =="y":
#ensure that the answer from last operation now becomes the first input      
      num1=first_answer
    elif choice =="n":
#while loop ends, thereby code ends      
      should_continue=False  
     
    else:
#for pesky users entering anything random other than y/n,make sure output from previous operation is stored
      num1=first_answer
      print("Incorrect value, please try again")
      break
calculator()
