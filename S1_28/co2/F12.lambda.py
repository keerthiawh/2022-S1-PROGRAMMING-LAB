l=int(input("enter the length"))
b=int(input("enter the breadth"))
h=int(input("enter the height"))
sqrArea=lambda l:l*l
print("area of square",sqrArea(l))
rectangleArea=lambda b,l:b*l
print("area of rectangle",rectangleArea(l,b))
triangleArea=lambda b,h:(b*h)/2
print("area of triangle",triangleArea(b,h))
