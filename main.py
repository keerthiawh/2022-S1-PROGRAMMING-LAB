import graphic 
from graphic import circle,rectangle
from graphic.tdgraphic import cubiod,sphere
from graphic.circle import *



print("area of a circle with radius 10 is:",circle.area_circle(10))
print("perimeter of a circle with radius 10 is",perimeter_circle(10))

print("area of circle with radius 10 is:",area_circle(10))

print("area of a rectangle with length and width 10 is:",rectangle.area_rec(10,10))
print("perimeter of a rectangle with length and width 10 is:",rectangle.perimeter_rec(10,10))

print("area of a cubiod with length,width,height 10 is:",cubiod.area_cuboid(10,10,10))
print("perimeter of a cuboid with length,width 10 is:",cubiod.perimeter_cuboid(10,10,10))

print("area of a sphere with radius 10 is:",sphere.area_sphere(10))
print("perimeter of a sphere with radius 10 is",sphere.perimeter_sphere(10))
