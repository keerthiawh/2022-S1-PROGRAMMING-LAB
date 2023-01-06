class Calc:
    def __init__(self):
        self.result=0
    def sum(self,num1,num2):
        self.result=num1+num2
        return self.result
    def sub(self,num1,num2):
        self.result=num1-num2
        return self.result
    def mul(self,num1,num2):
        self.result=num1*num2
        return self.result
    def div(self,num1,num2):
        self.result=num1/num2
        return self.result
calc1=Calc()
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice =int(input("Enter choice(1/2/3/4): "))
    if choice==5:
        break
    num1=float(input("enter a number"))
    num2=float(input("enter a number"))
    if choice == 1:
        result=calc1.sum(num1,num2)
    elif choice == '2':
        result=calc1.sub(num1,num2)
    elif choice == '3':
        result=calc1.mul(num1,num2)
    elif choice == '4':
        result=calc1.div(num1,num2)
    print("result",result)
    next_calculation = input("do next calculation? (y/n): ")



