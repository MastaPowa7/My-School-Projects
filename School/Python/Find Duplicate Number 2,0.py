import random

def main():
     Random_number_list = []
     User_number_list = []
     Duplicate_list = []
     max_numbers = 10

     for i in range(max_numbers):
          Random_number_list.append(random.randint(0,9))

     for i in range(max_numbers):
          User_number_list.append(int(input("Enter number: ")))

     for index1 in range(len(Random_number_list)):
          for index2 in range(len(Random_number_list)):
               if User_number_list[index1] == Random_number_list[index2]:
                    if index1 != index2:
                         Duplicate_list.append(index1)
     
     Results_list = Show_Results_List(Duplicate_list)
     Random_number_list.sort()
     print(Random_number_list)

     print(Results_list)
     
def Show_Results_List(Results_list):
     Return_Results_list = []

     for index in range(len(Results_list)):
          Result = Results_list.count(Results_list[index])
          if Results_list[index] not in Return_Results_list:
               Return_Results_list.append(f'{Results_list[index]} has {Result - 1} duplicates')
     
     Return_Results_list.sort()

     return Return_Results_list

main()


                         
