class bank():
    bankname:str
    bankacno:int
    bankbal:int

    def inputdata(self):
        self.bankname=input("enter the bank name:")
        self.bankacno=input("enter the bank account number:")
        self.bankbal=input("enter the bank balance:")

    def displaydata(self):
        print("bank name:",self.bankname)
        print("bank account number:",self.bankacno)
        print("bank balance:",self.bankbal)


#object creation

b=bank()
b.inputdata()
b.displaydata()