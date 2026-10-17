#Randomly generate lottery numbers, 4-10, ranging from 0-9
#Display lottery number amount
#Have user input numbers
#Run a check to see if each number is correct
     #First, run a for loop of "Index" in range(len(Lottery_Amount))
     #Then, have an if statement for if "User_List[Index]" == "Lottery_List[Index]"
          #If true, award $100 and move on
          #If false, move on
#Display the lottery numbers
#Display the total money earned and award $1000 if all numbers are correctly guessed

import random
def main():
     Lottery_number_amount = random.randint(4,10)
     Lottery_list = []
     User_list = []
     Money_earned = 0

     for i in range(Lottery_number_amount):
          Lottery_list.append(random.randint(0,9))

     print(f"Today's lottery contains {Lottery_number_amount} numbers.\n")

     for i in range(Lottery_number_amount):
          try:
               User_list.append(int(input("Enter a number: ")))

          except ValueError:
               print("Error... Try again\n")
               while True:
                    try:
                         User_list.append(int(input("Enter a number: ")))
                         break
                    except ValueError:
                         print("Error... Try again\n")

     for Index in range(len(Lottery_list)):
          if User_list[Index] == Lottery_list[Index]:
               Money_earned += 100
     
     print(f"\nToday's winning numbers are {print_lottery_list(Lottery_list)}.\nYou earned ${Money_earned:.2f}")

     if Money_earned / Lottery_number_amount == 100:
           Money_earned += 1000 / Lottery_number_amount
           print(f"+ {1000 / Lottery_number_amount:.2f} for guessing all winning numbers.\nTotal {Money_earned:.2f}\nSee you next week!")
     else:
          print("See you next week!")

def print_lottery_list(Lottery_list):
     result = ''
     for i in range(len(Lottery_list)):
          result += str(Lottery_list[i]) + ' ' if i < len(Lottery_list) -1 else str(Lottery_list[i])
     
     return result

main()

