# . Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
# find sum of 2 time.

class time:
    def __init__(self):
        self.__hour = int(input("Enter the hour:"))
        self.__minute = int(input("Enter the minute:"))
        self.__second = int(input("Enter the second:"))

    def __add__(self, other):
        hr = self.__hour+other.__hour
        mn = self.__minute+other.__minute
        sec = self.__second+other.__second
        if sec > 60:
            sec = sec-60
            mn = mn+1
        if mn > 60:
            mn = mn-60
            h = h+1
        print("Time is:", hr, ":", mn, ":", sec)
object1 = time()
object2 = time()
object1.__add__(object2)
