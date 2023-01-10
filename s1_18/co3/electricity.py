class electricitybill:

    def_init_(self):
        if self.unit<50:
            self.amount=self.unit*2.60
        elif self.unit<=100:
            
            self.amount=self.unit*3.25:
        elif self.unit<=200:
            self.amount=self.unit*5.26:
        
        elif self.unit>200:
            self.amount=self.unit*8.45+75
        else:
            print("invalid")
        def display(self):
            print("total amount= ",self.amount)

obj1=electricitybill()
obj1.calculate()
obj1.display()
obj2=electricitybill()
obj2.calculate()
obj2.display()
obj3=electricitybill()
obj3.calculate()
obj3.display()
