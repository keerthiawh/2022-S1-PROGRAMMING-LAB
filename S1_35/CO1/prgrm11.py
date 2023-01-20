sqr=lambda x:x*x
rect=lambda l,br:l*br
tri=lambda b,h:0.5*b*h

x=int(input("Enter side of square: "))
print(sqr(x))
l=int(input("Enter length of rectangle:"))
br=int(input("Enter breadth of rectangle:"))
print(rect(l,br))
b=float(input("Enter base of triangle:"))
h=float(input("Enter height of triangle:"))
print(tri(b,h))
