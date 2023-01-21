#Celcius to degree
def celcius(f):
    c=(f-32)/(5/9)
    printf("temperature in celcius = ",c)
    
def farenheit(c):
    f=(c*(9/5))+32
    printf("temperature in farenheit = ",f)

a=float(input("select choice--\n1.f to c\n2.c to f\n"))
if (a==1):
    x=float(input("enter the farenheit:"))
    celcius(x)
    
elif (a==2):
      x=float(input("enter the celcius:"))
      farenheit(x)
else:
    print("invalid")
