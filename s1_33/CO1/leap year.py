start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

if(start<end):
  print("list of leap years :")

for year in range(start, end):
     if year % 4 == 0 and year % 100 != 0:
        print(year)
  
