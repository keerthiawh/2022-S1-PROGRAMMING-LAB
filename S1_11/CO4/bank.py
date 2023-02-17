class bankacc:
    def __init__(self):
        self.name=input("enter name:")
        self.acc_no=input("enter acc no:")
        self.acc_type=input("enter acc type:")
        self.c_amt=0
    def deposit(self):
        self.depo_amt=int(input("enter amt to deposite"))
        self.c_amt=self.c_amt+self.depo_amt
    def withdraw(self):
        self.w_amt=int(input("enter amt withdraw"))
        if self.c_amt==0:
            print("sorry you have no balance")
        elif self.c_amt<self.w_amt:
            print("sorry you have no  sufficient balance")
        else:
            self.c_amt=self.c_amt-self.w_amt
    def display(self):
        print("name:",self.name)
        print("ac num:",self.acc_no)
        print("ac type:",self.acc_type)
        print("balance:",self.c_amt)
        
ob1=bankacc()
ob1.deposit()
ob1.display()
ob1.withdraw()
ob1.display()
