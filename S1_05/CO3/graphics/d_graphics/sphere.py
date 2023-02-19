import math
class sphere:
    def __init__(self,radius):
        self.radius=radius
    def surface_area(self):
        return 4*math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
