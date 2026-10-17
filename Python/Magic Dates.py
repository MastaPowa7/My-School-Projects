month = int(input("Enter a valid month in a numeric value: "))
day = int(input("Enter a valid day in a numeric value (for this exercise, 1-31 is allowed, even if that month doesn't have 31 days): "))
year = int(input("Enter a valid year. Must contain at least 2 digits: "))

while year >= 100:
     year -= 100
     if year < 100:
          break

if year >= 10 and 1 <= month <= 12 and 1 <= day <= 31:
     if month * day == year:
           result = "Magic Date!!!"               
     else:
          result = "No magic date..."
else:
      result = "You entered invalid information."

print(result)
