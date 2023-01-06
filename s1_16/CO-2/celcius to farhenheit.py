def celcius(f):
    c=(f-32)/(5/9)
    print("temperature in celcius =",c)
def farenheit(c):
    f=(c*(9/5))+32
    print("temperature in farhenheit=",f)
a=float(input("select choice-- \n1.f to c\n2.c to f\n"))
if (a==1):
    x=float(input("enter farhenheit"))
    celcius(x)
elif (a==2):
    x=float(input("enter celcius"))
    farenheit(x)
else:
    printf("invalid choice")
