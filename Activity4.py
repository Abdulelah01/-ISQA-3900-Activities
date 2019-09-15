def get_grade(marks):  # get_grade function will find the grade and return it to you
    percentage = (100 * marks) / 1000
    if 92 <= percentage <= 100:
        return "A+"
    elif 88 <= percentage <= 91.99:
        return "B+"
    elif 82 <= percentage < 87.99:
        return "C+"
    elif 78 <= percentage < 81.99:
        return "C"
    elif 70 <= percentage < 77.99:
        return "D+"
    elif 60 < percentage <= 69.99:
        return "D"
    else:
        return "D"


def display_title():  # display_title function will display the title
    print("Letter grade Calculator")


def main():
    display_title()
    while True:
        try:
            point = float(input("Enter the total number of points earned:"))
            print("You letter grade is : ", get_grade(point))
        except ValueError:
            print("Invalid input.")
            choice = input("Do you want to find another grade (y/n)")
            if choice == "y" or choice == "Y":
                continue
            if choice == "n" or choice == "N":
                print("Good Bye")
                break
main()
