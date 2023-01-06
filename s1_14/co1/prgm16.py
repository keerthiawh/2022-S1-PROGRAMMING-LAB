start=int(input("enter the start year:"))
end=int(input("enter the last year:"))
print("list of leap year:")
for year in range(start,end):
    if(year % 4 ==0)and (year % 100!=0):
        print(year)
