def celsius(f):
    
    c=(5/9)*(f-32)
    print("temperature in celsius=",c)

def farenheit(c):
    f=(c*(9/5))+32
    print("temperature in farenheit=",f)

a=float(input("select the choice-- \n1.f to c\n2.c to f\n"))
if (a==1):
        x=float(input("enter farenheit"))
        celsius(x)

elif (a==2):
    x=float(input("enter celsius"))
    farenheit(x)

else:
    print("invalid choice")
