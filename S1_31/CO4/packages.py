import graphics
from graphics import circle,rectangle
from graphics.tdgraphics import cuboid,sphere
print('area of circle with r=3 :',circle.area_circle(3))
print('perimeter of circle with r=3:',circle.perimeter_circle(3))
print('area of reactangle with l=2 and b=3 :',rectangle.area_rec(2,3))
print('perimeter of rectangle with l=2 and b=3:',rectangle.perimeter_rec(2,3))
print('area of cuboid with l=2 , b=3 ,h=4 :',cuboid.area_cuboid(2,3,4))
print('perimeter of cuboid with l=2 , b=3 , h=4:',cuboid.perimeter_cuboid(2,3,4))
print('area of sphere with r=5:',sphere.area_sphere(5))
print('perimeter of sphere with r=5:',sphere.perimeter_sphere(5))
