class government:
    president:str
    primeminister:str
    homeminister:str


    def inputdata(self):
        self.president=input("who is president of india?:")
        self.primeminister=input("who is primeminister of india?:")
        self.homeminister=input("who is homeminister of india?")

    def displaydata(self):
        print("president:",self.president)
        print("primeminister:",self.primeminister)
        print("homeminister:",self.homeminister)

gt=government()
gt.inputdata()
gt.displaydata()

