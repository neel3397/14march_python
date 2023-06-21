class employee:
    empid:int
    empname:str
    employeedepartment:str
    employeesalary:int

    def inputdata(self):
        self.empid=input("enter the id:")
        self.empname=input("enter the name:")
        self.employeedepartment=input("enter the department:")
        self.employeesalary=input("enter the salary:")

    def displaydata(self):
        print("student id",self.empid)
        print("student name:",self.empname)
        print("employeedepartment:",self.employeedepartment)
        print("employeesalary:",self.employeesalary)




st=employee()
st.inputdata()
st.displaydata()
