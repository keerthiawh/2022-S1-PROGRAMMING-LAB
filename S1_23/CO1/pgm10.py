start=int(input("enter start year:"))
end=int(input("enter end year:"))
for year in range(start-1,end+1):
    if(year%4==0)and (year%100!=0):
        print(year)
