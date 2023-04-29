class rectangle:
    length:int
    breadth:int
    area:int


    def getarea(self):
        self.length=int(input("enter the length of rectangle"))
        self.breadth=int(input("enter the breadth of rectangle"))
        self.area=self.length*self.breadth
        print("area of rectangle is",self.area)

r=rectangle()
r.getarea()