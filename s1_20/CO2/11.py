a=int(input("enter the side of square"))
square=lambda x:x*x
print("area of square is:",square(a))
b=int(input("enter length and breadth of rectangle"))
c=int(input())
rectangle=lambda x,y:(x*y)
print("area of rectangle is:",rectangle(b,c))
d=int(input("enter base and height of the triangle"))
e=int(input())
triangle=lambda x,y:(0.5*d*e)
print("area of triangle is:",triangle(d,e))
