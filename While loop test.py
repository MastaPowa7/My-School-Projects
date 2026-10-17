N= int(input('Type a number: '))
O= N
print(O)

while True:
    if O!=50:
        O += 1
        print(O)
    if O == 50:
        O += 1
        print(f'HI\n{O}')
    if O == 100:
        print('lol')
        break