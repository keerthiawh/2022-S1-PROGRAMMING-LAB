square=lambda x:x*x
rectangle=lambda l,br:l*br
triangle=lambda b,h,:0.5*b*h

x=int(input("enter the side of square:"))
print(square(x))
l=int(input("enter the length of reactangle"))
br=int(input("enter breadth of triangle"))
print(rectangle(l,br))
b=float(input("enter the base of triangle"))
h=float(input("enter the height of triangle"))
print(triangle(b,h))
