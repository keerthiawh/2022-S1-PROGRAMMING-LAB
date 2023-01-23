#Write lambda functions to find area of square, rectangle and triangle.
l = int(input("Enter the length: "))
b = int(input("Enter a beadth: "))
h = int(input("Enter the height: "))
area_square = lambda l: l*l
area_rectangle = lambda l, b: l*b
area_triangle = lambda l, b, h: 0.5*l*b*h
print("Area of square is: ", area_square(l))
print("Area of rectangle is: ", area_rectangle(l, b))
print("Area of triangle is: ", area_triangle(l, b, h))