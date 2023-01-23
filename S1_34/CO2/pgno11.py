area_square = lambda side : side * side
area_rectangle = lambda length,width : length * width
area_triangle =  lambda s,a,b,c : (s*(s-a)*(s-b)*(s-c)) ** 0.5

a=int(input("Enter the length"))
b=int(input("Enter the breadth"))
c=int(input("Enter the height"))
s = (a + b + c) / 2

print("Area of square=",area_square(a))
print("Area of rectangle=",area_rectangle(a,b))
print("Area of triangle=",area_triangle(s,a,b,c))
