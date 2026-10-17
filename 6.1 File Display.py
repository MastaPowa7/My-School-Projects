with open('numbers.txt','r') as File:
     for line in File:
          Value = int(line.strip())
          print(Value)