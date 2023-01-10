def celsius(f):
    c=(f-32)/(5/9)
    print("temperature in celsius = ",c)

def farenheat(c):
    f=(c * 9/5) + 32
    print("temp in farenheat = ",f)
a=float(input("select choice\n1.f to c\n2.c to f\n"))
if (a==1):
    y=float(input("enter farenheat"))
    celsius(y)

elif (a==2):
    y=float(input("enter celsius"))
    farenheat(y)

else:
     print("invalid")
    


