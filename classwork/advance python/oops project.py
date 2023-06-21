#class define for student
class student:
    #blank dictionary
     db={}
     
     #input method-which accept from student user
     
     def input(self):
         email=input("enter your mail")
         password=input("enter your password")

         #storing data in db
         #here email is key and and password is value

         self.db[email]=password
     def display(self):
          #display all students

          for k,v in self.db.items():
               print("email=",k)
               print("password=",v)
class faculty:
        db={}
        def inputdata(self):
            email=input("enter your email")
            password=input("enter your password")

            self.db[email]=password

        def display(self):
            for k,v in self.db.items():
                print("email=",k)
                print("password=",v)





#object creation of student class
f=faculty()
status=True
s1=student()
status=True
while status:

              






    data="""
      press 1 for student registration
      press 2 for faculty registration
      press 3 for view all students
      press 4 for exit"""

    print(data)
    user_input=int(input("enter your choice:"))
    if user_input==1:
         s1.input()

    
    elif user_input==2:
         f.inputdata()
       
    

    elif user_input==3:
         s1.display()

    else:
         status=False

    choice=input("do you want to perform more operations?")


    if choice=='n':
         status=False