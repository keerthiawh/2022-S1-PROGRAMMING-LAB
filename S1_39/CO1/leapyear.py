def checkLeap(year):
    if (( year%400 == 0) or
        ( year%4 == 0 ) and
        ( year%100 != 0)):
     print("given year is a leap year");
    else:
     print("given year is not a leap year");
year = int(input("enter year:"))
checkLeap(year)

          
