class Time:
    __hour=0
    __minute=0
    __second=0
    def __init__(self):
        self.__hour=int(input("enter the hour"))
        self.__minute=int(input("enter the minute"))
        self.__second=int(input("enter the second"))
    def __add__(self,other):
        h=self.__hour+other.__hour
        m=self.__minute+other.__minute
        s=self.__second+other.__second
        if s>60:
            s=s-60
            m=m+1
        if m>60:
            m=m-60
            h=h+1
        print("time is:",h,":",m,":",s)

obj1=Time()
obj2=Time()
obj1+obj2
        
