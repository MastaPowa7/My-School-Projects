import math
total_bugs = 0

for day in range(1, 6):
     bugs_collected = float(input(f'How many bugs were collected for day {day}: '))
     has_decimal = math.floor(bugs_collected)
     while bugs_collected % has_decimal != 0 or bugs_collected < 0:
          print('Error: Number must be a whole number and greater than zero.')
          bugs_collected = float(input(f'How many bugs were collected for day {day}: '))

     total_bugs += math.floor(bugs_collected)

print(f'Total bugs in {day} days: {total_bugs}')
