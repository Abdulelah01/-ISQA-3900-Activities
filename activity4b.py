def get_delivery_price(timeIndi,weight):
    if (timeIndi==2):
        if (weight<1.99):
            return 7.95
    else:
        extraWeight=int(weight-1.99)
        return (7.95 + extraWeight)

    if (weight<1.99):
                return 9.95
    else:
            extraWeight=int(weight-1.99)
    return (9.95 + extraWeight)

def display_title():#display_title function will display the title
    print(" \nMetropolitan delivery cost calculator")

def main():
    display_title()
    while True:#while loop untill user press n
        try:
            timeIndicator = int(input("Input the number 2 for 2 hours or less or the number 1 for 1 hour of delivery or less please:"))
            if (timeIndicator>2 or timeIndicator<0):
                print('The delivery time indicator must be between 1 or 2:')
                continue
            weight=float(input(" Enter the weight of your package in pounds please?"))
            if (weight>50 or weight<0):
                print(" The company does not accept a single package over 50 LBs.")
                continue
            print("\n The total delivery price for your package is: $",get_delivery_price(timeIndicator,weight))
        except ValueError:
                print(" Invalid input.")
        choice=input(" Do you want to find another cost (y/n)?\n")
        if (choice== "y" or choice== "Y"):
            continue
        if (choice=="n" or choice== "N"):
                print(" Good Bye")
                break
main()