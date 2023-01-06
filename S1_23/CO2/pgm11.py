sqr=lambda x:x*x
x=int(input("enter side of square: "))
print(sqr(x))

rect=lambda l,br:l*br
l=int(input("enter length of rectangle: "))
br=int(input("enter breadth of rectangle:  "))
print(rect(l,br))

tri=lambda b,h:0.5*b*h
b=float(input("enter base of triangle: "))
h=float(input("enter height of triangle: "))
print(tri(b,h))
