def main():
     userInput = input()
     cipherText = applyCipher(userInput)
     print(cipherText)

def applyCipher(userText):
     LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     shiftAmount = -1

     shiftText = ''
     for character in userText:
          character = character.upper()
          number = LETTERS.index(character) if character.isalpha() else number == None

          if character.isalpha():
               if character in LETTERS:
                    if number + shiftAmount >= 25:
                         index = (number - 26) + shiftAmount
                    else:
                         index = number + shiftAmount

                    shiftText += LETTERS[index]

     return shiftText

main()