def celsius(f):
    c=(f-32)/(5/9)
    print("tempreture in celsius= ",c)

def farenheit(c):
    f=(c*(9/5))+32
    print("tempreture in farenheit= ",f)

a=float(input("select choice--  \n1.F to C\n2.C to F\n"))
if (a==1):
    x=float(input("enter farenheit"))
    celsius(x)

elif (a==2):
    x=float(input("enter celsius"))
    farenheit(x)

else:
    print("invalid choice")
