square=lambda x:x*x
rectangle=lambda l,b:l*b
triangle=lambda b,h:0.5*b*h
x=int(input("Enter the side of square:"))
print(square(x))
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
print(rectangle(l,b))
b=float(input("Enter base of triangle:"))
h=float(input("Enter height of triangle:"))
print(triangle(b,h))
