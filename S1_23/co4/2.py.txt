class Bank:
    name=""
    current_balance=0
    acNo = 0
    def createAccount(self):
        if self.name == "" and self.acNo == 0:
            self.acNo = int(input("Enter account number: "))
            self.name = input("Enter name: ")
        else:
            print("Account already created This Object")
    def depositAccount(self):
        if self.acNo == 0 or self.name == "":
            print("Please create account first")
        elif self.current_balance == 0:
            self.current_balance = int(input("Enter amount to deposit: "))
        else:
            self.current_balance += int(input("Enter amount to deposit: "))
    def withdrawAccount(self):
        if self.acNo == 0 or self.name == "":
            print("Please create account first")
        elif self.current_balance == 0:
            print("sorry, you have no balance")
        else:
            amount= int(input("Enter amount to withdraw: "))
            if amount > self.current_balance:
                print(self.name , " sorry, you have insufficient balance")
            else:
                self.current_balance -= amount
    def displayAccount(self):
        if self.name == "" or self.acNo == 0:
            print("Please create account first")
        else:
            print("Account number: ", self.acNo)
            print("Name: ", self.name)
            print("Current balance: ", self.current_balance)

customers1 = Bank()
customers2 = Bank()
customers3 = Bank()

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Create account for customer 1 : 1")
        print("Create account for customer 2 : 2")
        print("Create account for customer 3 : 3")
        choiceC = int(input("Enter your choice: "))
        if choiceC == 1:
            customers1.createAccount()
        elif choiceC == 2:
            customers2.createAccount()
        elif choiceC == 3:
            customers3.createAccount()
        else:
            print("Invalid choice")
    elif choice == 2:
        print("Deposit for customer 1 : 1")
        print("Deposit for customer 2 : 2")
        print("Deposit for customer 3 : 3")
        choiceC = int(input("Enter your choice: "))
        if choiceC == 1:
            customers1.depositAccount()
        elif choiceC == 2:
            customers2.depositAccount()
        elif choiceC == 3:
            customers3.depositAccount()
        else:
            print("Invalid choice")
    elif choice == 3:
        print("Withdraw for customer 1 : 1")
        print("Withdraw for customer 2 : 2")
        print("Withdraw for customer 3 : 3")
        choiceC = int(input("Enter your choice: "))
        if choiceC == 1:
            customers1.withdrawAccount()
        elif choiceC == 2:
            customers2.withdrawAccount()
        elif choiceC == 3:
            customers3.withdrawAccount()
        else:
            print("Invalid choice")
    elif choice == 4:
        print("Display for customer 1 : 1")
        print("Display for customer 2 : 2")
        print("Display for customer 3 : 3")
        choiceC = int(input("Enter your choice: "))
        if choiceC == 1:
            customers1.displayAccount()
        elif choiceC == 2:
            customers2.displayAccount()
        elif choiceC == 3:
            customers3.displayAccount()
        else:
            print("Invalid choice")
    elif choice == 5:
        break