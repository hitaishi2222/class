# Leap year problem

year = int(input("Enter the year to check it is a leap year ot not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a not leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is a not leap year")
    