#Version 1.0
#Made 10/18/2025
#Last updated: 11:52am
#Last updated: 12/15 2:22am
import math, os, time, string

userStoredTimes = []
convertedStoredTime = ""

while(True):
     os.system('cls')
     print("IGT Calculator by MastaPowa7 \n")

     if len(userStoredTimes) > 0:
          print("Your times: \n")
          for i in range (0, len(userStoredTimes)):
               print(f"{userStoredTimes[i]}\n")
     print(f"Current elements: {len(userStoredTimes)}")

     userInput = input("Enter the times for each level. Type \"?\" for help: ")

     if userInput != "a" and not userInput.isalpha() and userInput not in string.punctuation:
               userStoredTimes.append(userInput)     
     elif userInput.lower() == "a" and userInput.isalpha():
          totalTimeInSeconds = 0

          if userStoredTimes:
                  for index in range(0 , len(userStoredTimes)):
                        isMinute = False
                        StrMinutes = ""
                        StrSeconds = ""

                        for element in (userStoredTimes[index]):
                              if element != ":" and not isMinute:
                                    if not ":" in userStoredTimes[index]:
                                          StrMinutes += "0"
                                          isMinute = True
                                    else:
                                          StrMinutes += element

                              elif element == ":":
                                    isMinute = True

                              if element != ":" and isMinute:
                                    StrSeconds += element
               
                        timeInSeconds = (int(StrMinutes) * 60) + float(StrSeconds)
                        totalTimeInSeconds +=  timeInSeconds
      #     else:
      #       print("No values have been entered...")
      #       time.sleep(1)
      #       input("Press Enter to continue...")
      #       continue
                

          convertedMinutes = math.floor(totalTimeInSeconds / 60)
          convertedSeconds = round(totalTimeInSeconds - (convertedMinutes * 60), 2)

          convertedStoredTime += str(convertedMinutes) + ":"
          if convertedSeconds > 10:
                convertedStoredTime += str(convertedSeconds)
          else:
                convertedStoredTime += "0" + str(convertedSeconds)

          print(f"Total time: {convertedStoredTime}")
          time.sleep(2)
          input("Press Enter to continue...")
          convertedStoredTime = ""
          continue
     elif userInput == "?":
           #os.system('cls')
           print("\nGUIDE: \n \"A\" - Calculates total times \n \"C\" - Clears all entered times \n \"E\" - Exits the program \n")
           time.sleep(2)
           input("Press Enter to exit...")
           continue
     elif userInput.lower() == "c" and userInput.isalpha():
           userStoredTimes = []
           os.system("cls")
           print("Cleared...")
           time.sleep(1)
           input("Press Enter to continue...")
           continue
     elif userInput.lower() == "e" and userInput.isalpha():
           exit()
     else:
           continue
     
