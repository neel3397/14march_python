"""encapsulation:it is a process which is used to wrap the data in single entity.


it is protects data from outside the class which provides more security to data

setter and getter:

setter is used for set the data and getter is used for get the data.

private mode:it is access modifier which is only accessible within the class.

symbol of private mode is __(double underscore)"""

#create class product

class product:

    #constructor define
    def __init__(self):
        self.__mobile=15000  #private mode
        self.laptop=20000

    #display method
    def display(self):
        print("mobile:",self.__mobile)
        print("laptop:",self.laptop)

    #change value through method
    def changedata(self,newmobileprice):
        self.__mobile=newmobileprice

obj=product()
obj.display()


obj.__mobile=20000
obj.laptop=60000
obj.display()
print("change data using method")

obj.changedata(70000)
obj.display()
