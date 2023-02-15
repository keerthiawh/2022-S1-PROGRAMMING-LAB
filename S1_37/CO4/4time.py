# . Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
# find sum of 2 time.

class time:
    def __init__(self):
        self.__hour = int(input("Enter the hour:"))
        self.__minute = int(input("Enter the minute:"))
        self.__second = int(input("Enter the second:"))

    def __add__(self, other):
        h = self.__hour+other.__hour
        m = self.__minute+other.__minute
        s = self.__second+other.__second
        if s > 60:
            s = s-60
            m = m+1
        if m > 60:
            m = m-60
            h = h+1
        print("Time is:", h, ":", m, ":", s)
object1 = time()
object2 = time()
object1.__add__(object2)

