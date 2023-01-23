starr=2022
end=(int(input("Enter end year:"))
if start<end
     print("list pf leap year between ",+str(start)+"and"+str(end)+":")
     while start<end:
         if start%4==0 and start%100!=0:
             print(start)
         if start%100==0 and start%400==0:
             print(start)
         start+=1
