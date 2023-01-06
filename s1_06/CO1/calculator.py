def add(x, y):
    return x+y

def substract(x, y);
    return x - y

def multiply(x, y):
    return x + y

def divide(x, y):
    return x / y


print("select operation.")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")

while True:
    choice=input("enter choice:(1/2/3/4):")

    if choice in ('1','2','3','4'):
        num1=float(input("enter first number:")
