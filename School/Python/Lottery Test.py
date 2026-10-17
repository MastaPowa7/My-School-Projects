import random

def main():
     Lottery_list = []
     User_list = []
     Lottery_amount = random.randint(4,8)
     Money = 0

     for i in range(Lottery_amount):
          Lottery_number = random.randint(1,9)
          Lottery_list.append(Lottery_number)

     print(f"Today's lottery contains {Lottery_amount} numbers.")

     for i in range(Lottery_amount):
          User_number = int(input("Enter a number: "))
          User_list.append(User_number)

     for i in range(Lottery_amount):
          if User_list[i] in Lottery_list:
               Money += 100
     
     print(f"Today's numbers are {Lottery_list}\nYou won ${Money}.")

main()
