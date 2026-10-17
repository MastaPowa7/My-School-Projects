import math
import time
import sys

def main():
     User_Input = int(input("Enter a number to find the square root of: "))
     X = User_Input
     Newton_SQRT = (X + (User_Input / X)) / 2
     Actual_SQRT = math.sqrt(User_Input)
     Count = 0
     print(f"   Number               Actual Square Root")

     while True:
          Count += 1
          X = Newton_SQRT
          Newton_SQRT = (X + (User_Input / X)) / 2
          print(f"{Count}) {Newton_SQRT:<20} {Actual_SQRT}")
          Format_Newton_SQRT = (f"{Newton_SQRT:.15f}")
          Format_Actual_SQRT = (f"{Actual_SQRT:.15f}")

          if Format_Newton_SQRT == Format_Actual_SQRT:
               break
          time.sleep(2)

def Do_You_Want_To_Repeat():
     Repeat = input("Enter another input? Type Y, else type anything to exit: ")

     if Repeat == "Y" or Repeat == "y":
          main()
     else:
          sys.exit()

main()
Do_You_Want_To_Repeat()

