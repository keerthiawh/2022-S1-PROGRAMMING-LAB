import packages
from packages import circle,rectangle
from packages .graphics import cuboid,sphere
print("enter the area of the circle:",circle.area_circle(6))
print("enter the perimeter of the circle:",circle.perimeter_circle(5))
print("enter the area of the rectangle:",rectangle.area_rectangle(7,5))
print("enter the perimeter of the rectangle:",rectangle.perimeter_rectangle(4,3))
print("enter the area of the cuboid:",cuboid.area_cuboid(4,3,2))
print("enter the perimeter of the cuboid:",cuboid.perimeter_cuboid(5))
print("enter the area of the sphere:",sphere.area_sphere(6))
print("enter the perimeter of the sphere:",sphere.perimeter_sphere(5))
