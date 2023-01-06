a=str(input("enter 1st string: "))
b=str(input("enter 2nd string: "))
def swapp(a, b):
    c= b[:2] + a[2:]
    d= a[:2] + b[2:]
    return c + ' ' + d
print(swapp(a,b))
