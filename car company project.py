class carshowroom:
    def company(self):
        self.cgst=0.1
        self.sgst=0.1
        self.insurance=1000000

        while True: 
           print("mg","tata")
           self.n=input("enter the car company")
           if self.n=="mg":
               print("welcome to mg")
               self.model()
               break
           elif self.n=="tata":
               print("welcome to tata")
               self.model()
               break
           else:
               print("invaild car company")
    def model(self):
        if self.n=="mg":
            while True:
                print("select from hector and gloster")
                self.choice=input("enter the car name")
                if self.choice=="hector":
                    self.price(self.choice)
                    break
                elif self.choice=="gloster":
                    self.price(self.choice)
                    break
                else:
                    print("invaild car model")
        elif self.n=="tata":       
            while True:
                print("select from nexon and punch")
                self.choice=input("enter the car name")
                if self.choice=="nexon":
                    self.price(self.choice)
                    break
                elif self.choice=="punch":
                    self.price(self.choice)
                    break
                else:
                    print("invaild car model")
    def price(self,choice):
        if choice=="hector":
            self.p=30000000
        elif choice=="gloster":
            self.p=50000000
        elif choice=="nexon":
            self.p=15000000
        elif choice=="punch":
            self.p=12000000
            total=self.p+(self.cgst*self.p)+(self.sgst*self.p)+self.insurance
            print(total)
q=carshowroom()
q.company()