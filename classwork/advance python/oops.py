"""
oops-object oriented programming structure

class-it is a blue print of object.

in python we can declare class as class keyword.

object-it is instance of a class

car-volvo,ciaz
student-name,subject


syntax:-
    class classname:
         statements

method:it will declare inside a class
function:it will declare outside a class

self:this is use to define that object is of this class.we have to write self compulsory.
"""
class student:
    stdid=1
    stdname="neel"

    def getdata(self):
        print("this is the data of students")

#object creation
st=student()
print(st.stdid)
print(st.stdname)
st.getdata()
