"""
constructor:it is special method that is called when object is created

the purpose of python constructor is to assign value to the data members within the class when an object is created.

constuctor method is always__init__.

1.default constuctor:which dont have parameters
2.parameterized constructor:which have parameters
"""


"""class student:
    def __init__(self,id,name):
        print("student id",id)
        print("student name",name)

s=student(3,"neel")"""


"""class employee:
    def __init__(self,id,name):
      self.id=id
      self.name=name

    def display(self):
        print("id:",self.id)
        print("name:",self.name)

emp1=employee(1,"neel")
emp2=employee(2,"richa")

emp1.display()
emp2.display()"""


#default constuctor

class default:
    def __init__(self):
        print("this is called default constuctor")
d=default()


class check:
    def __init__(self):
        print("this is first constuctor")

    def __init__(self):
        print("this is second constructor")

c=check()


class student:
    count=0
    def __init__(self):
        student.count=student.count+1

s1=student()
s2=student()
s3=student()
print("the number of student is",student.count)
