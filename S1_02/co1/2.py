start=int(input("Enter starting year:"))
end=int(input("Enter ending year:"))
print("leap years from ",start," to ",end," is:")
for year in range(start,end):
    if(0==year%4) and  (0!=year%100) or (0==year%400):
        print(year)
    