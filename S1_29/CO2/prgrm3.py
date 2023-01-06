def fahr():
    f=(c*(9/5))+32
    print("the fahrenheit value is:",f)
    

def cel():
    c=(f-32)*(5/9)
    print("the celsius value is:",c)
    
c=int(input("enter celsius value:"))
fahr()
f=int(input("enter the fahrenheit value:"))
cel()
