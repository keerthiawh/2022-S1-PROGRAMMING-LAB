#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to compare the area of 2 rectangles.

class rectangle:
    def __init__(self):
        self.__length = int(input("Enter the length:"))
        self.__width = int(input("Enter the width:"))

    def __lt__(self, other):
        if self.__length*self.__width < other.__length*other.__width:
            print("Area of rectangle 1 is less than rectangle 2")
        else:
            print("Area of rectangle 1 is greater than rectangle 2")
    
object1 = rectangle()
object2 = rectangle()
object1.__lt__(object2)


