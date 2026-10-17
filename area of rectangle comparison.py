rectangle1L = int(input("Enter the rectangle's length: ")) 
rectangle1W = int(input("Enter the rectangle's width: "))
rectangle2L = int(input("Enter the rectangle's length: ")) 
rectangle2W = int(input("Enter the rectangle's width: "))
rectangle1 = rectangle1L * rectangle1W
rectangle2 = rectangle2L * rectangle2W

if rectangle1 > rectangle2:
    print("Rectangle 1 has greater area")
else:
    if rectangle1 < rectangle2:
        print("Rectangle 2 has a greater area")
    else:
        print("Both rectangles have an equal area")
    

    