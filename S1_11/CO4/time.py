class time:
    __hour=0
    __minute=0
    __second=0
    def __init__(self):
        self.__hour=int(input("enter hour:"))
        self.__minute=int(input("enter minute:"))
        self.__second=int(input("enter second:"))
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
        print("time:",h,":",m,":",s)
time1=time()
time2=time()
result=time1+time2

