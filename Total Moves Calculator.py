import math
print('TOTAL MOVES CALCULATOR - MastaPowa7','\n=====================================\nThe purpsoe of this program is to determine to total number of moves you will have based on the number of moves until you take damage and your total health. Do not use decimals as this calculator only calculates whole numbers.\nPress Enter to begin',sep='')
input('')

xMoves_input= float(input('Enter moves amount : '))
if xMoves_input % 1 != 0:
    print('Nice try buddy ;)')
else:
    print('Ok')

xDamage_input= float(input('Enter damage amount: '))
if xDamage_input % 1 != 0:
    print('Nope :P')
else:
    print('Ok')

xHP_input= float(input('Enter health amount: '))
if xHP_input % 1 != 0:
    print("Let's see what this comes up with :O",'\n\nThe results:','\n============')
else:
    print('Ok','\n\nThe results:','\n============')
    
#Whole number converter
xMoves= xMoves_input//1
xDamage= xDamage_input//1
xHP= xHP_input//1

#Calculations
xDamageHP= math.ceil(xHP/xDamage)
xDamageHP_og= xHP/xDamage
xTotal= math.ceil(xDamageHP*xMoves)
xTotal_og= xDamageHP_og*xMoves

#Maff
print(f'Total moves: {xTotal}','\n',f'Total number of times you can be damaged: {xDamageHP:.0f}','\n',f'The Math: {xHP:.0f}/{xDamage:.0f} = {xDamageHP_og}, the number of times you can be damaged (rounds to {xDamageHP}). {xDamageHP_og} * {xMoves:.0f} = {xTotal_og}, the total number of moves (rounds to {xTotal} because moves amount is {xMoves:.0f}. You can fact check by taking {xHP:.0f} and subtracting it by {xDamage:.0f} {xDamageHP} time(s) until you reach 0 or below.")','\n\nPress Enter to exit',sep='')
input('')
