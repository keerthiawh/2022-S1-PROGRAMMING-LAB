start=int(input("enter start year:"))
end=int(input("enter last year:"))
print("list of leap years:")
for year in range(start,end):
    if (year %4 == 0) and (year % 100 !=0):
              print(year)
