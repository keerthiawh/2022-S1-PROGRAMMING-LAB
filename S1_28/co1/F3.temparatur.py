def celsius(f):
    c=(f-32)/(5/9)
    print("temperatur in celsius=",c)

def farenheit(c):
    f=(c*(9/5))+32
    print("temperature in farenheit=",f)
a=float(input("select choice--\n1.f to c\n2.c to f\n"))
if (a==1):
    x=float(input("enter the farenheit:"))
    celsius(x)
elif(a==2):
    x=float(input("enter the celsius:"))
    farenheit(x)
else:
    print("invalid choice")
