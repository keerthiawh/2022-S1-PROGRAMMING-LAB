str=input("enter a string:")
l=len(str)
if l>2:
    if str[-3:]=="ing":
        str+="ly"
        print("combined string is:",str)
    else:
            str+="ing"
else:
    print("too short")
