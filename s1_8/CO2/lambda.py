square=lambda x:x*x
rectangle=lambda l,br:l*br
triangle=lambda b,h:0.5*b*h
x=int(input("enter side of square:"))
print(square(x))
l=int(input("enter length of rectangle:"))
br=int(input("enter breadth of rectangle:"))
print(rectangle(l,br))
b=float(input("enter base of trangle:"))
h=float(input("enter height of triangle:"))
print(triangle(b,h))
