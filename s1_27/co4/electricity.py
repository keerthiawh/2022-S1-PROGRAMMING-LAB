class electricitybill():
    
    def read(self):
        self.unit=int(input("enter the unit:"))

    def calculate(self):
        if(self.unit<50):
            self.amount=self.unit*2.60
        elif(self.amount<=100):
            self.amount=self.unit*3.25
        elif(self.unit<=200):
            self.amount=self.unit*5.26
        else:
            if(self.unit>200):
                self.amount=(self.unit*8.45)+75

    def display(self):
         print(self.amount)

obj1=electricitybill()
obj1.read()


        
        
