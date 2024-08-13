year = int(input("Enter year you want to check = "))
def is_leap(year):

    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not a leap year")
    elif year % 4 == 0:
        print("Leap Year")
    else:
        print("Not a leap year")
    
    return False

is_leap(year)
