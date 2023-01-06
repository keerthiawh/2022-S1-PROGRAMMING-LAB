sqr=lambda x:x*x
rect=lambda l,br:l*br
tri=lambda b,h:0.5*b*h
x=int(input("enter side of square:"))
print(sqr(x))
l=int(input("enter the length of rectangle:"))
br=int(input("enter the breadth of rectangle:"))
print(rect(l,br))
b=float(input("enter base of triangle:"))
h=float(input("enter height of triangle:"))
print(tri(b,h))
