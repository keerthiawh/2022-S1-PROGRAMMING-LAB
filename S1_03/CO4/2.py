# Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class bank:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.accountno = int(input("Enter you account number: "))
        self.type = input("Enter your account type: ")
        self.current_amount = 0

    def deposit(self):
        self.d_amount = int(input("Enter the amount you are going to deposit: "))
        self.current_amount = self.current_amount + self.d_amount

    def withdraw(self):
        self.w_amount = int(input("Enter the amount  you are going to withdraw: "))
        self.current_amount = self.current_amount - self.w_amount

    def display(self):
        print("name:", self.name)
        print("account number:", self.accountno)
        print("account type:", self.type)
        print("balance amount:", self.current_amount)


obj1 = bank()
obj1.deposit()
obj1.display()
obj1.withdraw()
obj1.display()
