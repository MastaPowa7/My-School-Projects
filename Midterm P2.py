def is_prime (num, itt):
     if num < 2:
          return False
     itt = 0
     the_end = num
     for i in range (2, the_end):
          itt += 1
          ##print(f'Num = {the_end:<3}| I = {i:<3}| {num / i:<20}| {num % i:<3}')
          if num % i == 0:
               ##print("NOT A PRIME")
               return False, itt
     return True, itt
print ("The 25 prime numbers between 1 and 100:")
count=0
for num in range (1, 101):
     if is_prime (num):
          count=count+1
          print (count, num)