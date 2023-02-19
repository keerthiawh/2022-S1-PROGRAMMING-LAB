from graphics.rectangle import rectangle
from graphics.circle import circle
from graphics.d_graphics.cuboid import cuboid
from graphics.d_graphics.sphere import sphere

r=rectangle(5,6)
print("Rectangle area =",r.area())
print("Rectangle perimeter =",r.perimeter())

c=circle(5)
print("circle area =",c.area())
print("circle perimeter =",c.perimeter())

cb=cuboid(2,3,4)
print("cuboid surface area =",cb.surface_area())
print("cuboid perimeter =",cb.perimeter())

s=sphere(5)
print("sphere area =",s.surface_area())
print("sphere perimeter =",s.perimeter())
