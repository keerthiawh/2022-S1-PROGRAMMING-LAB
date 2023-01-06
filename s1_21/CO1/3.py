def celcius(f):
    c=(f-32)*(5/9)
    print("temperature in celcius is: ",c)

def fahrenheit(c):
    f=(c*(9/5))+32
    print("temperature in fahrenheit is: ",f)

a=int(input("select the conversion. 1:fahrenheit to celsius. 2:celsius to fahrenheit"))
if(a==1):
    x=float(input("enter the temperature in fahrenheit:"))
    celcius(x)
elif(a==2):
    y=float(input("enter the temperature in celsius:"))
    fahrenheit(y)
else:
    print("invalid")

