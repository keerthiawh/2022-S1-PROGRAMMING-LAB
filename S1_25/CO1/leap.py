start=int(input("enter the current year"))
end=int(input("enter the end year"))
if start<end:
    print("leap years between",start,"and",end)
    while start<end:
        if start%4==0 and start%100!=0:
            print(start)
        if start%100==0 and start%400==0:
            print(start)
        start=start+1    
