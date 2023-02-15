class Bankacc():
    def __init__(self):
        self.depositor_name=input("enter the name of the depositor:")
        self.acc_no=int(input("enter the account number:"))
        self.acc_type=input("enter the account type:")
        self.current_amount=0
    def deposit(self):
        self.depo_amount=int(input("enter the amount to deposit:"))
        self.current_amount=self.current_amount+self.depo_amount
    def withdraw(self):
        self.withdraw_amount=int(input("enter the amount to the withdraw:"))
        self.current_amount=self.current_amount-self.withdraw_amount
    def display(self):
        print("NAME OF DEPOSITOR:",self.depositor_name)
        print("ACC_NUMBER:",self.acc_no)
        print("ACC_TYPE:",self.acc_type)
        print("BALANCE:",self.current_amount)
obj1=Bankacc()
obj1.deposit()
obj1.display()
obj1.withdraw()
obj1.display(