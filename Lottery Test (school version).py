import random

def main():
     Lottery_list = []
     Lottery_amount = 7

     for i in range(Lottery_amount):
          Lottery_number = random.randint(1,9)
          Lottery_list.append(Lottery_number)
     
     print(f"Today's numbers are:")
     for i in range(Lottery_amount):
          print(Lottery_list[i], end="")
          
main()
