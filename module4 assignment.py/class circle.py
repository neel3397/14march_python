class circle:
    radius:float
    area:float


    def getarea(self):
        self.radius=float(input("enter the radius of circle"))
        self.area=3.14*self.radius*self.radius
        print("area of circle is",self.area)

c=circle()
c.getarea()