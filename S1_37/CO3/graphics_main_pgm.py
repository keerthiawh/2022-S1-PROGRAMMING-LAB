import graphics
from graphics import circle,rectangle
from graphics.tdgraphics import cuboid,sphere
from graphics.circle import *

print("Area of circle is:",circle.area_circle(6))
print("Perimeter of circle is:",circle.perimeter_circle(22))


print("Area of Rectangle is:",rectangle.area_rect(6,10))
print("Perimeter of Rectangle is:",rectangle.perimeter_rect(22,5))


print("Area of Cuboid is:",cuboid.area_cuboid(6,7,8))
print("Perimeter of Cuboid is:",cuboid.perimeter_cuboid(2,4,10))


print("Area of sphere is:",sphere.area_sphere(6))
print("Perimeter of sphere is:",sphere.perimeter_sphere(22))
