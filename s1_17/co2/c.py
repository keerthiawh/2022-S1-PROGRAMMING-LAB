def celsius(f):
    c=(f-32)*(5/9)
    print("temp in celsius=",c)

def farenheit(c):
    f=(c*(9/5)+32)
    print("temp in farenheit=",f)

a=float(input("select choice--\n1.f to c\n2.c to f\n"))
if (a==1):
    y=float(input("enter farenheit"))
    celsius(y)

elif(a==2):
    y=float(input("enter celsius"))
    farenheit(y)              

else:
    print("invalid")
    
