# I'm aware this isn't exactly what we were supposed to do, but because I couldn't complete the concept containment Thursday due to me not knowing how to calculate a running total using for, I figured this example would allow me to learn as I already know how to solve this normally.
import math
total_bugs = 0
days_tracked = int(input('How many days are you tracking: '))

while days_tracked < 0:
     print('Error: Number must be a whole number and greater than zero.')
     days_tracked = int(input('How many days are you tracking: '))

day_results = []

for day in range(1, days_tracked + 1):
     print(f'How many bugs were collected for day {day}:')
     bugs_collected = float(input())
     #rounds user input to later be used for a decimal check
     has_decimal = math.floor(bugs_collected)
     #checks to see if user input is a whole number or greater than 0
     while bugs_collected % has_decimal != 0 or bugs_collected < 0:
          print('Error: Number must be a whole number and greater than zero.')
          print(f'How many bugs were collected for day {day}:')
          bugs_collected = float(input())
     total_bugs += math.floor(bugs_collected)
     day_results.append(f'Day {day} has {bugs_collected}')

average = total_bugs / days_tracked
add_s = ''
if days_tracked > 1:
     add_s = 's'

print(f'Total bugs in {day} day{add_s}: {total_bugs}\nAverage bugs of total: {average}\nResults:')
for day_result in day_results:
     print(day_result)