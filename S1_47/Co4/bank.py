class bank:
    def __init__(self):
        self.name=input("enter your name:")
        self.accountno=int(input("enter your account number"))
        self.type=input("N enter your account type:")
        self.current_amount=0
        
    def deposit(self):
        self.d_amount=int(input("enter the amount you are going to deposit"))
        self.current_amount=self.current_amount+self.d_amount
    def withdraw(self):
        self.w_amount=int(input("enter the amountyou are going to withdraw"))
        self.current_amount=self.current_amount-self.w_amount
    def display(self):
        
        print("name",self.name)
        print("amount number ",self.accountno)
        print("account type",self.type)
        print("balance amount",self.current_amount)
obj1=bank()
obj1.deposit()
obj1.display()
obj1.withdraw()
obj1.display()

                           
