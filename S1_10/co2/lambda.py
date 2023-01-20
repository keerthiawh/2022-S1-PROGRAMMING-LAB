sqr=lambda x:x*x
rect=lambda l,y:l*y
tri=lambda b,h:0.5*b*h
x=int(input("enter side of square: "))
print(sqr(x))
l=int(input("enter length of rectangle: "))
y=int(input("enter breadth of rectangle: "))
print(rect(l,y))
b=float(input("enter base of triagle: "))
h=float(input("enter height of triangle: "))
print(tri(b,h))
