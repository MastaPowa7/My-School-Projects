RNumeral_input = int(input("Enter a number between 1 and 10: "))

if RNumeral_input == 1:
     RNumeral = "I"
else:
     if RNumeral_input == 2:
          RNumeral = "II"
     else:
          if RNumeral_input == 3:
               RNumeral = "III"
          else:
               if RNumeral_input == 4:
                    RNumeral = "IV"
               else:
                    if RNumeral_input == 5:
                         RNumeral = "V"
                    else:
                         if RNumeral_input == 6:
                              RNumeral = "VI"
                         else:
                              if RNumeral_input == 7:
                                   RNumeral = "VII"
                              else:
                                   if RNumeral_input == 8:
                                        RNumeral = "VIII"
                                   else:
                                        if RNumeral_input == 9:
                                             RNumeral = "IX"
                                        else:
                                             if RNumeral_input == 10:
                                                  RNumeral = "X"
                                             else:
                                                  RNumeral = "Invalid input."

print(RNumeral)
