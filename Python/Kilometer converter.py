
CONVERTION_FACTOR = 0.6214
def main():
     kilometers = float(input("Enter the kilometers: "))
     show_miles(kilometers)

def show_miles(kilometers):
     miles = kilometers * CONVERTION_FACTOR
     print(f"{kilometers} kilometers converts to {miles:.3f} miles.")

main()
