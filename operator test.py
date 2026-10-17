num1 = int(input('enter number: '))
num2 = int(input('enter second number: '))
num3 = input('enter math operator (only the first letter): ')

if num3 == 'a':
    operator = '+'
elif num3 == 's':
    operator = '-'
elif num3 == 'm':
    operator = '*'
elif num3 == 'd':
    operator = '/'

total = (f'{num1} {operator} {num2}')
print (total)
