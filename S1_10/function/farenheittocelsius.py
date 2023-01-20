def celcius(f):
    c=(f-32)/(5/9)
    print("temparature in celcius = ",c)

def farenheit(c):
    f=(c*(9/5))+32
    print("temprature in farenheit = ",f)

a=float(input("select choice-- \n1.f to c\n2.c to f\n"))
if (a==1):
    x=float(input("enter farenheit"))
    celcius(x)

elif (a==2):
    x=float(input("enter celcius"))
    farenheit(x)

else:
    print("invalid choice")
    
