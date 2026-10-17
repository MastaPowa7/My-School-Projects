import random
def main():
     list = []
     matching_list = []
     add_to_list = 0
     max_content = 0
     duplicate = 0

     for i in range(10):
          add_to_list = random.randint(1, 10)
          list.append(add_to_list)
          max_content += 1
     
     print(f'{list}\nmax_content = {max_content}')

     for list_number in range(0, max_content):
          for list_check in range(max_content):
               if list_number != list_check:
                    if list[list_number] ==  list[list_check]:
                         duplicate += 1
                         matching_list.append(f'{list[list_number]} has {duplicate} duplicates.')
                         ##print(f' {list[list_number]} has a duplicate.')
          duplicate = 0

     print(matching_list)


main()