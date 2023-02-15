class Time:
    __hour=0
    __minute=0
    __second=0
    def __init__(self):
        self.__hour=int(input("Enter the hour:"))
        self.__minute=int(input("Enter the minute:"))
        self.__second=int(input("Enter the second:"))
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
        print("Time is:",h,":",m,":",s)

    

        
        

obj1=Time()
obj2=Time()
obj1+obj2

    
