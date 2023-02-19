class cuboid:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height

    def surface_area(self):
        return 2*(self.length*self.width+self.width*self.height+self.height*self.length)

    def perimeter(self):
        return 4*(self.length+self.width+self.height)
    
