class Bankaccount:
    def __init__(self):
        accountname=input("enter accountname:")
        accountnumber=int(input("enter accountnumber:"))
        accounttype=input("account type:")
        self.balance=0

    def deposit(self):
        amount=int(input("enter amountto be deposited:"))
        self.balance=amount
        print("amount deposited is:",amount)

    def withdrawl(self):
        amount=int(input("enter amount to be withdraw:"))
        if self.balance>=amount:
            self.balance=amount
            print("amount withdraw:",amount)
        else:
            print("balance is insufficient")

    def display(self):
        print("available balance:",self.balance)

s=Bankaccount()
s.deposit()
s.withdrawl()
s.display()
