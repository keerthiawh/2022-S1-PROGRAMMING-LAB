#Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class Bank:
    name=""
    current_balance=0
    acNo = 0
    def createAccount(self):
        self.acNo = int(input("Enter account number: "))
        self.name = input("Enter name: ")
    def depositAccount(self):
        if self.acNo == 0 and self.name == "":
            print("Please create account first")
        elif self.current_balance == 0:
            self.current_balance = int(input("Enter amount to deposit: "))
        else:
            self.current_balance += int(input("Enter amount to deposit: "))
    def withdrawAccount(self):
        if self.acNo == 0 and self.name == "":
            print("Please create account first")
        elif self.current_balance == 0:
            print("sorry, you have no balance")
        else:
            amount= int(input("Enter amount to withdraw: "))
            if amount > self.current_balance:
                print("sorry, you have insufficient balance")
            else:
                self.current_balance -= amount
    def displayAccount(self):
        print("Account number: ", self.acNo)
        print("Name: ", self.name)
        print("Current balance: ", self.current_balance)

b1 = Bank()

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        b1.createAccount()
    elif choice == 2:
        b1.depositAccount()
    elif choice == 3:
        b1.withdrawAccount()
    elif choice == 4:
        b1.displayAccount()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
