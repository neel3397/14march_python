class student:
    stdid:int
    stdname:str


    def inputdata(self):
        self.stdid=input("enter the id:")
        self.stdname=input("enter the name:")

    def displaydata(self):
        print("student id",self.stdid)
        print("student name:",self.stdname)


#object creation

st=student()
st.inputdata()
st.displaydata()