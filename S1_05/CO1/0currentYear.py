#Display future leap years from current year to a final year entered by user.

year = int(input("Enter starting year: "))
finalYear = int(input("Enter final year: "))
while year <= finalYear:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)
    year += 1
