import sys
calculation_attempt = 0
print("Basic Calculator\n================")
def main():
     global calculation_attempt
     calculation_attempt += 1
     is_first_operation = True
     answer = 0
     print(f"Calculation #{calculation_attempt}")
     while True:
          #Choose first number
          if is_first_operation:
               user_input = input("Enter the first number. (Type 'exit' to exit): ")
               if user_input != "exit":
                    answer = float(user_input)
               elif user_input == "exit":
                    system_exit()

          #Choose an operator
          is_first_operation = False
          def get_operator(operator):
               operator = input("Enter the operator (Type ? for help): ")
               return operator
          
          operator = None
          if operator == None:
               operator = get_operator(operator)
          while operator == "?":
               operator_hotkeys(answer)
               operator = get_operator(operator)
          
          if operator == "C":
               print("Cleared\n")
               break
          elif operator == "exit":
               system_exit()
          elif operator not in ("+", "-", "*", "/", "V", "I", "S", "E"):
               print("Error: Invalid operator\n")
               continue
          elif operator in ("+", "-", "*", "/"):
               #Choose next number
               numberB = float(input("Enter the next number: "))

          #Operator check
          if operator == "+":
               answer = add_numbers(answer, numberB)
          elif operator == "-":
               answer = subtract_numbers(answer, numberB)
          elif operator == "*":
               answer = multiply_numbers(answer, numberB)
          elif operator == "/":
               while numberB == 0:
                    print("Cannot divide by 0")
                    numberB = float(input("Enter the next number: "))
               answer = divide_numbers(answer, numberB)
          elif operator == "V":
               answer = reciprocal(answer)
          elif operator == "I":
               answer = inverse(answer)
          elif operator == "S":
               if answer < 0:
                    print("Error: Cannot find square root of a negative number\n")
                    continue
               else:
                    answer = square_root(answer)
          elif operator == "E":
               answer = exponential(answer)

          if answer % 1 == 0:
               answer = int(answer)
               print(f"Answer: {answer}\n")
          else:
               print(f"Answer: {answer}\n")

def operator_hotkeys(number_1):
     print("Hotkeys:")
     print("+ - Addition")
     print("- - Subtraction")
     print("* - Multiplication")
     print("/ - Division")
     print("V - Reciprical")
     print("I - Inverse")
     print("S - Square Root")
     print("E - Exponential")
     print("C - Clear")
     print("exit - Exit")
     return number_1

def system_exit():
     print("Exiting...")
     sys.exit()

#Math functions
def add_numbers(number_1, number_2):
     return number_1 + number_2

def subtract_numbers(number_1, number_2):
     return number_1 - number_2

def multiply_numbers(number_1, number_2):
     return number_1 * number_2

def divide_numbers(number_1, number_2):
     return number_1 / number_2

def reciprocal(number_1):
     return 1 / number_1

def inverse(number_1):
     return -1 * number_1

def square_root(number_1):
     return number_1 ** 0.5

def exponential(number_1):
     return number_1 ** 2

while True:
     main()