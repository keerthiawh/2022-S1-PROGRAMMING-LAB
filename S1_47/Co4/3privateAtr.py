#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to compare the area of 2 rectangles.
class Time:
    __hour = 0
    __minute = 0
    __second = 0

    def _init_(self):
        self.__hour = int(input("Enter the hour:"))
        self.__minute = int(input("Enter the minute:"))
        self.__second = int(input("Enter the second:"))

    def _add_(self, other):
        h = self._hour+other._hour
        m = self._minute+other._minute
        s = self._second+other._second
        if s > 60:
            s = s-60
            m = m+1
        if m > 60:
            m = m-60
            h = h+1
        print("Time is:", h, ":", m, ":", s)


obj1 = Time()
obj2 = Time()
obj1._add_(obj2)

