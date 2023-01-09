x=int(input("Enter the first element:"))  
y=int(input("Enter the second element:")) 
def gcd(x, y):
    if (x==0):
        return y
    if (y==0):
        return x
    if (x==y):
        return x
    if (x>y):
        return gcd(x-y,y)
    return gcd(x,y-x)
if(gcd(x,y)):
    print("GCD of",x,"and",y,"is",gcd(x, y))
