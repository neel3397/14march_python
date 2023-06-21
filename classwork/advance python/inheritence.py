"""
inheritence:when one class inherits from another is called inheritence

parent class:base class
child class:derived class or sub class

child class can access all the properties of parent class

types of inheritence:

1:single level inheritence:
   class a
     |
     |
    class b"""

'''class parent:
    def house(self):
        print("3 bhk house")

class child(parent):
    def car(self):
        print("bmw")

#object
c=child()
c.house()
c.car()'''



"""2:multi-level inheritence:
a-b-c"""

'''class parent:
    def house(self):
        print("3 bhk house")

class child(parent):
    def car(self):
        print("bmw")

#object
c=child()
c.house()
c.car()'''

'''class grandparent:
    def vh1(self):
        print("cycle")


class parent(grandparent):
    def vh2(self):
        print("scooter")

class child(parent):
    def vh3(self):
        print("bike")


#object
c=child()
c.vh1()
c.vh2()
c.vh3()'''


"""3:multiple inheritence:a+b=c"""

'''class calculation1:
    def summation(self,a,b):
        return a+b

class multiplication:
    def multiplication(self,a,b):
        return a*b
    
class derived(calculation1,multiplication):
    def divide(self,a,b):
        return a/b
    
d=derived()
print(d.summation(20,30))
print(d.multiplication(40,60))
print(d.divide(20,40))'''

"""4-hierarchical inheritence:more than one derived class created from single base class."""


'''class parent:
    def fun1(self):
        print("this fuction is parent class")

class child1(parent):
    def fun2(self):
        print("this fuction is child1")
class child2(parent):
    def fun3(self):
        print("this fuction is child 2")

c1=child1()
c2=child2()
c1.fun1()
c1.fun2()
c2.fun1()
c2.fun3()'''


"""5:hybrid inheritence:it is combination of different inheritence"""



class school:
    def fun1(self):
        print("this function in school")

class student1:
    def fun2(self):
        print("this function in student1")

class student2(school):
    def fun3(self):
        print("this fuction in student2")

class student3(student1,school):
    def fun4(self):
        print("this function is student3")

object=student3()
object.fun1()
object.fun2()
object.fun4()
